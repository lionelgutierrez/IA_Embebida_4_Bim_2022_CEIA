/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include "platform/mbed_thread.h"

int main()
{
    DigitalOut myled(LED2);
    Serial uartUsb(USBTX, USBRX);

 while (1) {
        if( uartUsb.readable() ) {
            myled = 1;
            char receivedChar = uartUsb.getc();
            uartUsb.putc(receivedChar);
            wait(0.9);
            myled = 0;
            
        }
    }
}
