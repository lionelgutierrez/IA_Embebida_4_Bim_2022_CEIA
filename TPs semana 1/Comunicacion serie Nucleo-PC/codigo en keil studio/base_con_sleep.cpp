/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include "platform/mbed_thread.h"

// millisegundos durante los cuales mando a dormir al micro
#define SLEEP_RATE     100ms
#define MAXIMUM_BUFFER_SIZE 1

int main()
{
    DigitalOut myled(LED2);
    BufferedSerial uartUsb(USBTX, USBRX);    
    
    char receivedChar[MAXIMUM_BUFFER_SIZE] = {0};
    uint32_t num;

     while (1) {
        if( uartUsb.readable() ) {
                myled = 1;
                num = uartUsb.read(receivedChar, sizeof(receivedChar));
                if (num) {
                    uartUsb.write(receivedChar, num);
                }
                
        }
        ThisThread::sleep_for(SLEEP_RATE);
        myled = 0;
     }
}
