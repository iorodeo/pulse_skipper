#define __STDC_LIMIT_MACROS
#include <util/atomic.h>
#include <stdint.h>
#include <Streaming.h>

// Constants
enum {
    DISPLAY_BINARY = 0, 
    DISPLAY_NUMBER = 1
    };
const int PULSE_INPUT_PIN = 2;
const int PULSE_OUTPUT_PIN = 3;
const int INTERRUPT_NUMBER = 0;

enum {NUM_COUNTER_BITS=8};
const int COUNTER_OUTPUT_PINS[NUM_COUNTER_BITS] = {5,6,7,8,9,10,11,12};

const unsigned long MAX_PERIOD = 40000; 
const unsigned long PULSE_HIGH_FRAC = 3;

// Global variables
bool pulseHigh = false;
unsigned int skipPulse = 0;
unsigned long pulseCount = 0;
unsigned long pulseTime = 0;
unsigned long pulseTimeLast = 0;
unsigned int displayMode = DISPLAY_NUMBER;

// Function prototypes
void onPulseInterrupt();
void resetOutpuPulse();
void setOuputCounterBits(unsigned short count);

void setup() {
    Serial.begin(9600);
    pinMode(PULSE_INPUT_PIN,INPUT);
    pinMode(PULSE_OUTPUT_PIN,OUTPUT);
    for (int i=0; i<NUM_COUNTER_BITS; i++) {
        pinMode(COUNTER_OUTPUT_PINS[i],OUTPUT);
    }
    digitalWrite(PULSE_INPUT_PIN, LOW);
    digitalWrite(PULSE_OUTPUT_PIN, LOW);
    attachInterrupt(INTERRUPT_NUMBER,onPulseInterrupt,RISING);
}

void loop() {
    int cmd;
    unsigned long pulseCountCopy;

    resetOutputPulse();

    while(Serial.available() > 0) {

        cmd = Serial.read();
        switch (cmd) {

            // Skip a upto 9 pulses - this is super cheesey
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
                    skipPulse = ((unsigned int)cmd) - 48;
                }
                break;

            case 'r':
                // Reset pulse count 
                ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
                    pulseCount = 0;
                }
                break;

            case 'c':
                // Return pulse count
                ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
                    pulseCountCopy = pulseCount;
                }
                Serial << pulseCountCopy << ", ";
                Serial << pulseCountCopy%(1<<NUM_COUNTER_BITS) << endl;
                break;

            case 'b':
                displayMode = DISPLAY_BINARY;
                break;

            case 'n':
                displayMode = DISPLAY_NUMBER;
                break;
                
            default:
                break;
        }
    }
}



void resetOutputPulse() {
    unsigned long dt;
    unsigned long period;
    unsigned long currentTime; 
    unsigned short pulseCount8Bit;

    if (pulseHigh) {
        period = pulseTime - pulseTimeLast;
        if (period > MAX_PERIOD) {
            period = MAX_PERIOD;
        }
        ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
            currentTime = micros();
            // Note, need to change to handle wrap around
            dt = currentTime - pulseTime;
            if (dt > period/PULSE_HIGH_FRAC) {
                digitalWrite(PULSE_OUTPUT_PIN, LOW);
                pulseHigh = false;
                pulseCount8Bit = pulseCount%(1<<NUM_COUNTER_BITS);
                setCounterOutputBits(pulseCount8Bit);
            }
        }
    }
}

void setCounterOutputBits(unsigned short count) {
    if (displayMode == DISPLAY_BINARY) {
        for (int i=0; i<NUM_COUNTER_BITS; i++) {
            digitalWrite(COUNTER_OUTPUT_PINS[i], 0x01 &(count>>i));
        }
    }
    else {
        for (int i=0; i<NUM_COUNTER_BITS; i++) {
            if ( i < count%(NUM_COUNTER_BITS+1) ) {
                digitalWrite(COUNTER_OUTPUT_PINS[i], HIGH);
            }
            else {
                digitalWrite(COUNTER_OUTPUT_PINS[i], LOW); 
            } 
        }
    }
}

void onPulseInterrupt() {
    if (skipPulse>0) {
        skipPulse -= 1;
    }
    else {
        digitalWrite(PULSE_OUTPUT_PIN, HIGH);
        pulseHigh = true;
        pulseTimeLast = pulseTime;
        pulseTime = micros();
    }
    pulseCount += 1;
}

