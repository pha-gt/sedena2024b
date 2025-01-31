String inputString = "";        // Cadena reservada
bool stringComplete = false;    // Bandera de completado

void setup() {
  Serial.begin(9600);           // Initialize Baudrade:
  inputString.reserve(200);     // reserva 200 bytes
}

void loop() {
  if (stringComplete) {         // Cuando el mensaje se recibio
    Serial.println(inputString);// Muestra el mensaje
    inputString = "";           // Limpia la cadena
    stringComplete = false;     // Reinicia bandera
  }
}

/*
  Ocurre cuando un dado es registrado al RX serial
*/
void serialEvent() {
  while (Serial.available()) {.  //Mientras reciba datos
  
    char inChar = (char)Serial.read();   //convierte los bytes a char
    inputString += inChar;               //concatena el caracter a inputString
    if (inChar == '\n') {                //Si hay un caracter de nueva line
      stringComplete = true;             // define fin del mensaje
    }
  }
}
