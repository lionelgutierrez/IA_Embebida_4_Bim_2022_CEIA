/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include "platform/mbed_thread.h"

int main()
{
    DigitalOut led(LED2);
    Serial uartUsb(USBTX, USBRX);
    char buffer[50];
    
 while (1) {
        if( uartUsb.readable() ) {
            uartUsb.scanf("%s", &buffer);
            led = 1;
            uartUsb.printf( "Soy la nucleo. Recibi un dato: ");
            uartUsb.printf("%s", buffer);
            uartUsb.printf( "\r\n");
            wait(0.9);
            led = 0;
            wait(0.9);
        }
    }
}
