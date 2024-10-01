d={1: 100}

f={
  "LineSpacing": "FullSize",
  "WrapMode": "ByWords",
  "HorizontalAlignment": "Center",
  "LeftMargin": 0,
  "RightMargin": 0,
  "TopMargin": 0,
  "BottomMargin": 0,
  "Rectangle": {
    "LLX": 60,
    "LLY": 354,
    "URX": 536,
    "URY": 420
  },
  "Rotation": 0,
  "SubsequentLinesIndent": 0,
  "VerticalAlignment": "None",
  "Lines": [
    {
      "HorizontalAlignment": "Center",
      "Segments": [
        {
          "Value": "My Physics Topic",
          "TextState": {
            "FontSize": 34,
            "Font": "PlaywriteDEGrund-Regular",
            "ForegroundColor": {
              "A": 255,
              "R": 118,
              "G": 70,
              "B": 82
            },
            "BackgroundColor": {
              "A": 0,
              "R": 0,
              "G": 0,
              "B": 0
            },
            "FontStyle": "Bold",
            "FontFile": "PlaywriteDEGrund-Regular.ttf"
          }
        }
      ]
    }
  ]
}

print(f["Lines"][0]["Segments"][0]["Value"])