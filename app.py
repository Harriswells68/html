import streamlit as st
import time
import requests
import math

coverpaget={
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
coverpagen={
  "LineSpacing": "FullSize",
  "WrapMode": "ByWords",
  "HorizontalAlignment": "Center",
  "LeftMargin": 0,
  "RightMargin": 0,
  "TopMargin": 0,
  "BottomMargin": 0,
  "Rectangle": {
    "LLX": 235,
    "LLY": 220,
    "URX": 560,
    "URY": 366
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
            "FontSize": 20,
            "Font": "LeagueSpartan-Black",
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
            "FontStyle": "Regular",
            "FontFile": "LeagueSpartan-Black.ttf"
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
    "LLX": 30,
    "LLY": 357,
    "URX": 565,
    "URY": 562
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
    "LLX": 380,
    "LLY": 280,
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
            "FontSize": 14,
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

def designs(name, ptopic):
    global topic, radio
    if len(ptopic)>50:
        l=topic.split()
        m=math.ceil(len(l)/2)
        t1=""
        t2=""
        for i in range(m):
            t1=t1+l[i]+" "
        for i in range(m, len(l)):
            t2=t2+l[i]+" "
        ptopic=t1+'\n\n'+t2
    pdfn=name.replace(" ", "")
    url = "https://api.aspose.cloud/connect/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": "1f47805e-0b4f-4b93-abe1-c30901a65320",
        "client_secret": "7ca7be919737bce1cb80489209a0412d"
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
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
         print(f"An error occurred: {e}")
    time.sleep(5)
    for i in range(len(datas)):
        pn=0
        data=datas[i].copy()
        if i in [0, 1]:
            pn=1
        else:
            pn=i
        if i in [0, 1, 3]:
            if i==0:
     jus           data["Lines"][0]["Segments"][0]["Value"]=ptopic.upper()
            elif i==1 or i==3:
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

if c1:
    b1.empty()
    l1.success("Processing Please Wait")
    designs(name, topic)