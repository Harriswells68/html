import streamlit as st
import time
import requests
import math

idn=0
skeys=['d1f45e836c53f961c43126869c877332', '60c0c520be44a5752af2e25079cebd84', '7e851e8ef8ac3e2c875345105442bf54', 'cf2c98accb2e6dce7922c545d8fcd901', '0245776c0f7833a4a505b6f7c4918a9b', 'f9efba5f25cc46b2a3249bcb8824a6fb']
ids=['ba102dcc-a9d4-4328-85ab-bd624b097943', '607927a0-565d-4aa9-a25b-539ee8d8dc35', '08419b96-1f3f-4709-8ae7-74822a88b9dc', '22a45393-614b-436f-8361-8c9976bb43f2', 'd5eba395-0dd9-411b-8007-a4ac2a6c8265', '000a012f-607f-49c2-9e11-ee0cdd0860ef']

coverpaget={
  "LineSpacing": "FullSize",
  "WrapMode": "ByWords",
  "HorizontalAlignment": "Center",
  "LeftMargin": 0,
  "RightMargin": 0,
  "TopMargin": 0,
  "BottomMargin": 0,
  "Rectangle": {
    "LLX": 30,
    "LLY": 354,
    "URX": 566,
    "URY": 554
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
            "FontSize": 25,
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
coverpagen={
  "LineSpacing": "FullSize",
  "WrapMode": "ByWords",
  "HorizontalAlignment": "Center",
  "LeftMargin": 0,
  "RightMargin": 0,
  "TopMargin": 0,
  "BottomMargin": 0,
  "Rectangle": {
    "LLX": 295,
    "LLY": 198,
    "URX": 530,
    "URY": 348
  },
  "Rotation": 0,
  "SubsequentLinesIndent": 0,
  "VerticalAlignment": "None",
  "Lines": [
    {
      "HorizontalAlignment": "Center",
      "Segments": [
        {
          "Value": "SUJAL GARASIYA",
          "TextState": {
            "FontSize": 21,
            "Font": "LeagueSpartan-Bold",
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
            "FontFile": "LeagueSpartan-Bold.ttf"
          }
        }
      ]
    }
  ]
}

certi={
  "LineSpacing": "FullSize",
  "WrapMode": "ByWords",
  "HorizontalAlignment": "Center",
  "LeftMargin": 0,
  "RightMargin": 0,
  "TopMargin": 0,
  "BottomMargin": 0,
  "Rectangle": {
    "LLX": 15,
    "LLY": 357,
    "URX": 565,
    "URY": 555
  },
  "Rotation": 0,
  "SubsequentLinesIndent": 0,
  "VerticalAlignment": "None",
  "Lines": [
    {
      "HorizontalAlignment": "Center",
      "Segments": [
        {
          "Value": "topic",
          "TextState": {
            "FontSize": 16,
            "Font": "SourceSerif4-Regular",
            "ForegroundColor": {
              "A": 255,
              "R": 0,
              "G": 0,
              "B": 0
            },
            "BackgroundColor": {
              "A": 0,
              "R": 0,
              "G": 0,
              "B": 0
            },
            "FontStyle": "Regular",
            "FontFile": "SourceSerif4-Regular.ttf"
          }
        }
      ]
    }
  ]
}
ackn={
  "LineSpacing": "FullSize",
  "WrapMode": "ByWords",
  "HorizontalAlignment": "Center",
  "LeftMargin": 0,
  "RightMargin": 0,
  "TopMargin": 0,
  "BottomMargin": 0,
  "Rectangle": {
    "LLX": 368,
    "LLY": 265,
    "URX": 540,
    "URY": 300
  },
  "Rotation": 0,
  "SubsequentLinesIndent": 0,
  "VerticalAlignment": "None",
  "Lines": [
    {
      "HorizontalAlignment": "Center",
      "Segments": [
        {
          "Value": "SUJAL GARASIYA",
          "TextState": {
            "FontSize": 16,
            "Font": "SourceSerif4-Regular",
            "ForegroundColor": {
              "A": 255,
              "R": 0,
              "G": 0,
              "B": 0
            },
            "BackgroundColor": {
              "A": 0,
              "R": 0,
              "G": 0,
              "B": 0
            },
            "FontStyle": "Regular",
            "FontFile": "SourceSerif4-Regular.ttf"
          }
        }
      ]
    }
  ]
}
datas=[coverpaget, coverpagen, certi, ackn]

fail=False

def designs(name, ptopic):
    global topic, radio, idn, skeys, fail
    fail=False
    pdfn=name.replace(" ", "")
    url = "https://api.aspose.cloud/connect/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": ids[idn],
        "client_secret": skeys[idn]
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    response = requests.post(url, data=data, headers=headers, timeout=30)
    token = response.json()  # Assuming the response is in JSON format
    tk=token['access_token']
    try:
      url = f"https://api.aspose.cloud/v3.0/pdf/storage/file/{pdfn}.pdf"
      headers = {
      "Content-Type": "accept: multipart/form-data",
      "Authorization": f"Bearer {tk}"  # Replace with your actual bearer token
      }
      with open(f'Frontpages.pdf', 'rb') as file:
        files={'file': file}
        response = requests.put(url, headers=headers, files=files, timeout=30)
        if response.status_code==403:
            idn=idn+1
            designs(name, ptopic)
            fail=True
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
         print(f"An error occurred: {e}")
    time.sleep(5)
    if fail!=True:
      for i in range(len(datas)):
          pn=0
          data=datas[i].copy()
          if i in [0, 1]:
              pn=1
          else:
              pn=i
          if i in [0, 1, 3]:
              if i==0:
                  data["Lines"][0]["Segments"][0]["Value"]=ptopic.upper()
              elif i==1:
                data["Lines"][0]["Segments"][0]["Value"]=name.upper()
              elif i==3:
                  data["Lines"][0]["Segments"][0]["Value"]=name.upper()
          if i==2:
              stra=checker(name, topic, radio)
              data["Lines"][0]["Segments"][0]["Value"]=stra
          try:
              url = f"https://api.aspose.cloud/v3.0/pdf/{pdfn}.pdf/pages/{pn}/text"
              headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {tk}",
                "x-aspose-client": "Containerize.Swagger"
              }
              data = data
              # Add a timeout to the request to handle potential network issues
              response = requests.put(url, headers=headers, json=data, timeout=30)
              response.raise_for_status()
              print("Request successful!")
          except requests.exceptions.RequestException as e:
              print(f"An error occurred: {e}")
      time.sleep(3)
      try:
          url = f"https://api.aspose.cloud/v3.0/pdf/storage/file/{pdfn}.pdf"
          headers = {
            "Content-Type": "accept: multipart/form-data",
            "Authorization": f"Bearer {tk}"  # Replace with your actual bearer token
          }
          # Add a timeout and stream the response to handle large files
          response = requests.get(url, headers=headers, timeout=60)
          time.sleep(2)
          with open(f"pdfs/{pdfn}.pdf", "wb") as file:
              file.write(response.content)
      except requests.exceptions.RequestException as e:
          print(f"An error occurred: {e}")
      download(f"{pdfn}.pdf")

def download(file):
    global b1, l1
    with open(f"pdfs/{file}", "rb") as f:
      b1.download_button("Download pdf", f, file, "application/pdf")
    l1.success("Download your file")

def checker(name, topic, radio):
    if len(topic)<=50:
        if radio=="He/his":
            stra=f"This is to certify that\n\n{name.upper()}\n\nhas satisfactorily carried out his Physics Project on\n\n“{topic.upper()}”\n\nThe candidate himself did all the work under my supervision. His\n\n approach towards the subject and this project is sincere."
        elif radio=="She/her":
            stra=f"This is to certify that\n\n{name.upper()}\n\nhas satisfactorily carried out her Physics Project on\n\n“{topic.upper()}”\n\nThe candidate herself did all the work under my supervision. Her\n\n approach towards the subject and this project is sincere."
    else:
        l=topic.split()
        m=math.ceil(len(l)/2)
        t1=""
        t2=""
        for i in range(m):
            t1=t1+l[i]+" "
        for i in range(m, len(l)):
            t2=t2+l[i]+" "
        if radio=="He/his":
            stra=f'This is to certify that\n\n{name.upper()}\n\nhas satisfactorily carried out his Physics Project on\n\n“{t1.upper()}\n\n{t2.upper()}"\n\nThe candidate himself did all the work under my supervision. His\n\n approach towards the subject and this project is sincere.'
        elif radio=="She/her":
            stra=f'This is to certify that\n\n{name.upper()}\n\nhas satisfactorily carried out her Physics Project on\n\n“{t1.upper()}\n\n{t2.upper()}"\n\nThe candidate herself did all the work under my supervision. Her\n\n approach towards the subject and this project is sincere.'
    return stra

st.title("Certificate Generator")
st.caption("By Sujal❤️")

name=st.text_input("Enter Your Name")
topic=st.text_input("Enter your physics topic")
radio=st.radio("Your Pronouns", ['He/his', 'She/her'])

b1=st.empty()
c1=b1.button("Done")

l1=st.empty()

st.caption('If you got any errors please contact me:) ')

if c1:
    b1.empty()
    l1.success("Processing Please Wait")
    designs(name, topic)