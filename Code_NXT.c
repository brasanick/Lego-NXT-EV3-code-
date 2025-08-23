
// THIS CODE IS BASED ON NXC (Not Exacly C).
// Probably if you put this on VS Code, will appear a lot of errors.
// Try use the BricxCC IDE for a better experience.

#define Light_Sensor IN_1               // Light sensor defined on port 1
#define THRESHOLD 30                    // 30% of reflection
#define EV3_CONN 1                      // Bluetooth connection with EV3
#define INBOX 1                         // Mail Box (EV3 --> NXT)
#define OUTBOX 1                        // Out (NXT --> EV3)

task main() {
    SetSensorLight(Light_Sensor);       // Set the sensor as reflected light
    ClearScreen();                      // Clear the screen of NXT

    //I'll try to make a menu on NXT screen latter.


    while (true) {
        int mensagem;
        ReceiveRemoteNumber(INBOX, true, mensagem);                 // Recive message from EV3

        if (mensagem == 5) {
            TextOut(10, LCD_LINE2, "Motor Blocked");
            TextOut(10, LCD_LINE3, "Checking the light...");

            int reflexao = Sensor(Light_Sensor);                    // Read the value from 0 to 100 (%)

            if (reflexao > THRESHOLD) {
                SendRemoteNumber(EV3_CONN, OUTBOX, 1);              // Send '1' to EV3
                TextOut(10, LCD_LINE5, "Wall detected!");
                TextOut(10, LCD_LINE6, "Sending '1' to EV3");
            } else {
                SendRemoteNumber(EV3_CONN, OUTBOX, 0);              // Send '0' to EV3
                TextOut(10, LCD_LINE5, "Body detected!");
                TextOut(10, LCD_LINE6, "Sending '0' to EV3");
            }
        }

        Wait(500);  
    }
}
