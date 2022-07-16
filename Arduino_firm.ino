#include <Adafruit_GFX.h> // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735
#include <SPI.h>
#include <Fonts/FreeSerif9pt7b.h>

#define TFT_CS 10
#define TFT_DC 9
#define TFT_RST 8

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

String x;


void setup(void) {
  Serial.begin(115200);
  Serial.println("I am OK!");
  Serial.setTimeout(100);
  tft.initR(INITR_BLACKTAB);
  tft.setTextWrap(true); // Allow text to run off right edge
  tft.fillScreen(ST77XX_BLACK);
  tft.setRotation(1);
}


void loop(void){
  while (!Serial.available());
  x = Serial.readString();
  tft.setCursor(6, 4);
  tft.setTextSize(1);
  tft.setTextColor(ST77XX_WHITE, ST77XX_BLACK);
  tft.print(x);
  tft.drawLine(0, 0, 160, 0, 0xFA20);
  tft.drawLine(0, 40, 160, 40, 0xFA20);
  tft.drawLine(0, 55, 160, 55, 0xFA20);
  tft.drawLine(0, 80, 160, 80, 0xFA20);
  }
