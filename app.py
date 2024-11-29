import streamlit as st
import time
import datetime
import pickle
import requests
import math
import os

idn = 0

try:
    os.mkdir("pdfs")
except FileExistsError:
    pass

with open(r"cur.dat", "rb") as fp:
    d = pickle.load(fp)
    idn = d["idn"]

ci = ['d5c7df3a-8df0-4073-a3a1-733b9c75cc60', '4d1c06b0-5f74-47ec-a28f-9a3aea0fbba7', 'ba269dfb-0133-4ff6-9305-28a28c70e20f', 'af2ef260-5e6f-4b18-8301-0647d9b02443', '7f94fbae-bf94-4a68-9a57-e18cfb98b708', '834f77f6-b5ae-480e-a390-950363b9effe', '460e0c98-cba5-4029-94c9-9ba6885ec923', 'f11aebde-d3b0-4824-be99-62bd196882d5', '87a214f6-dac1-4994-b469-f71c434ab313', '316b12de-cd29-4141-8ce5-d735d932780a', '7215ac67-5f83-46a8-9e05-5314508067e4', '2c3ee1ce-29e6-4582-bc37-bebb41ff8c71', 'd8c4f831-fbdb-4819-a952-3dc70cdd541c', 'cee13fe5-f1b1-487d-8cac-6ad3b67f8357', 'dd14906f-92f4-4655-9bfd-517c7d978033', 'd2872cf5-20a2-41c3-a2f3-d3387b56eee1', '237f7f1d-a137-483e-9ac0-695f9c1945a0', 'a5c7304f-281f-45f5-b5e5-79bf5ae757a0', '80addd91-067c-432d-b9e7-48e8fb4c705d', '3ac75190-df71-4886-bcbb-9b69e90e3c84', 'ad17d7f5-d0eb-4137-aaff-06c05f1de6b1', '96f3d336-6960-4c9b-8568-5144382ac670', '68d541bb-2379-4a00-bda1-d7e9ee9a9f9c', 'af99f46e-1121-4e74-8eb8-c37b862e8b13', '26eeef2c-ff31-4670-8bdf-f128fd61cd14']
cs = ['819bcc40043c88f2321cc507081437ea', 'f01b375aaabd9af54f4671a7a781200f', 'd80886afcd91eb038305727fec10e741', '1a57301b134d7181b5328ee02866ecc8', 'b336a506bfc6f1e28a1aefd77b39dbd5', 'e213bcb098e7e1432ab8b1f1e73a89fe', 'd2e238eb2b843c2ed30d8618c811311f', '2b8e6e01aa5459bf8862b72ce5fbe5f3', '010385bafe66da384ff398f73a59bcee', 'cef8f777c8d652219ad7b96e5eaa18e6', '8dcbc98fe9e4ee36e36f304f8fd61c3b', 'eb8d5e3a91a8d46cb8aa5a0570e43511', '21318d3c9d2947b89131e1a47ead7935', '87d157628d29d026423dec8b40c72c40', 'f326556197fcca9d03a953ad496d232e', '1280339a366875e6184888d74d4c1606', 'c0446c576d2020fbde3adcac895e73c0', '8dd2dad52558ff9c4da38a8b27a4905a', '7d8c1b2a0a161c459e677605d6c4d0a5', '4c948ae411bb4c73dca17814c9a9794a', '2b8cdaa33e4437daabd2b4c0b7e4721a', 'bea34e5c070d6ec9f572cdd5f4282649', '7a16a37b943931baacf7ce3cc6b0b305', '2d8e78fcc7c4bb13601996df2385b3f1', '17b3bdd3b1a57cecbe77f9ce99db9a25']

def checkOverflow(name, topic=None):
    name = name.upper()

    b1 = len(name) > 21
    b2 = len(topic) > 25
    b3 = len(topic) > 40
    b4 = len(topic) > 60

    if len(name) > 21:
        name = name.split()
        f = math.ceil(len(name)/2)
        n1 = ""
        n2 = ""
        for i in range(f):
            n1 = n1+name[i]+" "
        for i in range(f, len(name)):
            n2 = n2+name[i]+" "
        n1 = n1.strip()
        n2 = n2.strip()

        name = (n1, n2)

    topic = topic.upper()

    if len(topic) > 25:
        topic = topic.split()
        f = math.ceil(len(topic)/2)
        t1 = ""
        t2 = ""
        for i in range(f):
            t1 = t1+topic[i]+" "
        for i in range(f, len(topic)):
            t2 = t2+topic[i]+" "
        t1 = t1.strip()
        t2 = t2.strip()
        topic = (t1, t2)

    if len(topic) <= 25:
        return (name, topic, b1, b2, b3, b4)

    elif len(topic) > 25:
        return (name, topic, b1, b2, b3, b4)


def genTuple(subject, name, cls, sec, pron, topic):
    try:
        nameconfig = {
            "LineSpacing": "FontSize",
            "WrapMode": "NoWrap",
            "HorizontalAlignment": "Center",
            "LeftMargin": 0,
            "RightMargin": 0,
            "TopMargin": 0,
            "BottomMargin": 0,
            "Rectangle": {
                "LLX": 310,
                "LLY": 167,
                "URX": 568,
                "URY": 207
            },
            "Rotation": 0,
            "SubsequentLinesIndent": 0,
            "VerticalAlignment": "Center",
            "Lines": [
                {
                    "HorizontalAlignment": "Center",
                    "Segments": [
                        {
                            "Value": "MOHAMMAD ZIYAN PATHAN\nXII C",
                            "TextState": {
                                "FontSize": 20,
                                "Font": "LeagueSpartan-Bold",
                                "ForegroundColor": {
                                    "A": 0,
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
                                "FontFile": "LeagueSpartan-Bold.ttf"
                            }
                        }
                    ]
                }
            ]
        }

        topicconfig = {
            "LineSpacing": "FullSize",
            "WrapMode": "ByWords",
            "HorizontalAlignment": "Center",
            "LeftMargin": 0,
            "RightMargin": 0,
            "TopMargin": 0,
            "BottomMargin": 0,
            "Rectangle": {
                "LLX": 30,
                "LLY": 300,
                "URX": 566,
                "URY": 335
            },
            "Rotation": 0,
            "SubsequentLinesIndent": 0,
            "VerticalAlignment": "None",
            "Lines": [
                {
                    "HorizontalAlignment": "Center",
                    "Segments": [
                        {
                            "Value": "SEMICONDUCTORS AND LEDEDP",
                            "TextState": {
                                "FontSize": 26,
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

        certconfig = {
            "LineSpacing": "FullSize",
            "WrapMode": "ByWords",
            "HorizontalAlignment": "Center",
            "LeftMargin": 0,
            "RightMargin": 0,
            "TopMargin": 0,
            "BottomMargin": 0,
            "Rectangle": {
                "LLX": 15,
                "LLY": 370,
                "URX": 565,
                "URY": 570
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

        acknconfig = {
            "LineSpacing": "FullSize",
            "WrapMode": "ByWords",
            "HorizontalAlignment": "Center",
            "LeftMargin": 0,
            "RightMargin": 0,
            "TopMargin": 0,
            "BottomMargin": 0,
            "Rectangle": {
                "LLX": 348,
                "LLY": 280,
                "URX": 550,
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
        r = checkOverflow(name, topic)
        nameconfig["Lines"][0]["Segments"][0]["Value"] = str(
            r[0])+'\n'+cls+' '+sec
        acknconfig["Lines"][0]["Segments"][0]["Value"] = (
            str(r[0]).lower()).title()
        topicconfig["Lines"][0]["Segments"][0]["Value"] = r[1]

        if pron == "He/his":
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0]}\n\nhas satisfactorily carried out his {subject} Project on\n\n“{topic.upper()}”\n\nThe candidate himself did all the work under my supervision. His\n\n approach towards the subject and this project is sincere.'
        if pron == "She/her":
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0]}\n\nhas satisfactorily carried out her {subject} Project on\n\n“{topic.upper()}”\n\nThe candidate herself did all the work under my supervision. Her\n\n approach towards the subject and this project is sincere.'
        if pron == 'He/his' and r[2] and not r[4]:
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0][0]+" "+r[0][1]}\n\nhas satisfactorily carried out his {subject} Project on\n\n“{topic.upper()}”\n\nThe candidate himself did all the work under my supervision. His\n\n approach towards the subject and this project is sincere.'
        if pron == 'She/her' and r[2] and not r[4]:
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0][0]+" "+r[0][1]}\n\nhas satisfactorily carried out her {subject} Project on\n\n“{topic.upper()}”\n\nThe candidate herself did all the work under my supervision. Her\n\n approach towards the subject and this project is sincere.'
        if pron == 'He/his' and r[4] and not r[2]:
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0]}\n\nhas satisfactorily carried out his {subject} Project on\n\n“{r[1][0]}\n\n{r[1][1]}”\n\nThe candidate himself did all the work under my supervision. His\n\n approach towards the subject and this project is sincere.'
        if pron == 'She/her' and r[4] and not r[2]:
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0]}\n\nhas satisfactorily carried out her {subject} Project on\n\n“{r[1][0]}\n\n{r[1][1]}”\n\nThe candidate herself did all the work under my supervision. Her\n\n approach towards the subject and this project is sincere.'
        if pron == 'He/his' and r[2] and r[4]:
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0][0]+" "+r[0][1]}\n\nhas satisfactorily carried out his {subject} Project on\n\n“{r[1][0]}\n\n{r[1][1]}”\n\nThe candidate himself did all the work under my supervision. His\n\n approach towards the subject and this project is sincere.'
        if pron == 'She/her' and r[2] and r[4]:
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0][0]+" "+r[0][1]}\n\nhas satisfactorily carried out his {subject} Project on\n\n“{r[1][0]}\n\n{r[1][1]}”\n\nThe candidate herself did all the work under my supervision. Her\n\n approach towards the subject and this project is sincere.'
        if pron == "He/his" and subject=="English":
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0]}\n\nhas satisfactorily carried out his {subject} Project on\n\n“{topic.upper()}”\n\nThe candidate himself did all the work under my supervision. His\n\n approach towards the subject and this project is sincere.'
        if pron == "She/her" and subject=="English":
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0]}\n\nhas satisfactorily carried out her {subject} Project on\n\n“{topic.upper()}”\n\nThe candidate herself did all the work under my supervision. Her\n\n approach towards the subject and this project is sincere.'
        if pron == "He/his" and subject=="Physical Education":
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0]}\n\nhas satisfactorily carried out his {subject} Project on\n\n“{topic.upper()}”\n\nThe candidate himself did all the work under my supervision. His\n\n approach towards the subject and this project is sincere.'
        if pron == "She/her" and subject=="Physical Education":
            certconfig["Lines"][0]["Segments"][0]["Value"] = f'This is to certify that\n\n{r[0]}\n\nhas satisfactorily carried out her {subject} Project on\n\n“{topic.upper()}”\n\nThe candidate herself did all the work under my supervision. Her\n\n approach towards the subject and this project is sincere.'


        if r[2]:
            nameconfig["Lines"][0]["Segments"][0]["Value"] = r[0][0] + \
                '\n'+r[0][1]+'\n'+cls+' '+sec
            acknconfig["Lines"][0]["Segments"][0]["Value"] = (
                (r[0][0]+'\n'+r[0][1]).lower()).title()
            nameconfig["Rectangle"] = {
                "LLX": 310,
                "LLY": 147,
                "URX": 568,
                "URY": 207
            }
            acknconfig["Rectangle"] = {
                "LLX": 348,
                "LLY": 260,
                "URX": 550,
                "URY": 300
            }

        if r[3]:
            topicconfig["Lines"][0]["Segments"][0]["Value"] = r[1][0]+'\n'+r[1][1]
            topicconfig["Rectangle"] = {
                "LLX": 30,
                "LLY": 265,
                "URX": 566,
                "URY": 360
            }

        if r[4] and subject!="English":
            topicconfig["Lines"][0]["Segments"][0]["Value"] = topic.upper()
            certconfig["Rectangle"] = {
                "LLX": 15,
                "LLY": 340,
                "URX": 565,
                "URY": 540
            }
            topicconfig["Rectangle"] = {
                "LLX": 30,
                "LLY": 265,
                "URX": 566,
                "URY": 370
            }
            topicconfig["Lines"][0]["Segments"][0]["TextState"]["FontSize"] = 24

        if r[5] and subject!="English":
            topicconfig["Lines"][0]["Segments"][0]["Value"] = topic.upper()
            certconfig["Rectangle"] = {
                "LLX": 15,
                "LLY": 340,
                "URX": 565,
                "URY": 540
            }
            topicconfig["Rectangle"] = {
                "LLX": 30,
                "LLY": 245,
                "URX": 566,
                "URY": 370
            }
            topicconfig["Lines"][0]["Segments"][0]["TextState"]["FontSize"] = 24

        return (nameconfig, topicconfig, certconfig, acknconfig)

    except Exception as e:
        print(e)
        return None


def designs(subject, name, cls, sec, pron, topic):
    global idn, b1, l1, w1

    if name!="" and topic!="":

        try:
            datak = genTuple(subject, name, cls, sec, pron, topic)

            n = ((name.replace(' ', '')).lower()+(subject.lower()).replace(' ', ''))

            indexEr = False
            downpdf = True

            while True:
                try:
                    url = "https://api.aspose.cloud/connect/token"
                    data = {
                        "grant_type": "client_credentials",
                        "client_id": ci[idn],
                        "client_secret": cs[idn]
                    }
                    headers = {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Accept": "application/json"
                    }
                    response = requests.post(
                        url, data=data, headers=headers, timeout=30)
                    token = response.json()
                    tk = token['access_token']

                    if subject == "English":
                        url = f"https://api.aspose.cloud/v3.0/pdf/storage/file/copy/english.pdf?destPath={n}.pdf&srcStorageName=pdfs&destStorageName=pdfs"
                        headers = {
                            "Content-Type": "application/json",
                            "Authorization": f"Bearer {tk}",
                            "x-aspose-client": "Containerize.Swagger"
                        }
                        response = requests.put(url, headers=headers, timeout=30)
                        response.raise_for_status()
                        print("Copied successful!")

                        for i in range(1, 4):
                            url = f"https://api.aspose.cloud/v3.0/pdf/{n}.pdf/pages/{i}/text"
                            headers = {
                                "Content-Type": "application/json",
                                "Authorization": f"Bearer {tk}",
                                "x-aspose-client": "Containerize.Swagger"
                            }
                            if i < 2:
                                i = i-1

                            response = requests.put(
                                url, headers=headers, json=datak[i], timeout=60)
                            response.raise_for_status()
                            print("Request successful!")

                        break

                    elif subject == "Physical Education":
                        url = f"https://api.aspose.cloud/v3.0/pdf/storage/file/copy/physicaleducation.pdf?destPath={n}.pdf&srcStorageName=pdfs&destStorageName=pdfs"
                        headers = {
                            "Content-Type": "application/json",
                            "Authorization": f"Bearer {tk}",
                            "x-aspose-client": "Containerize.Swagger"
                        }
                        response = requests.put(url, headers=headers, timeout=30)
                        response.raise_for_status()
                        print("Copied successful!")

                        for i in range(1, 4):
                            url = f"https://api.aspose.cloud/v3.0/pdf/{n}.pdf/pages/{i}/text"
                            headers = {
                                "Content-Type": "application/json",
                                "Authorization": f"Bearer {tk}",
                                "x-aspose-client": "Containerize.Swagger"
                            }
                            if i < 2:
                                i = i-1

                            response = requests.put(
                                url, headers=headers, json=datak[i], timeout=60)
                            response.raise_for_status()
                            print("Request successful!")

                        break

                    else:
                        url = f"https://api.aspose.cloud/v3.0/pdf/storage/file/copy/{(subject.lower()).replace(' ', '')}.pdf?destPath={n}.pdf&srcStorageName=pdfs&destStorageName=pdfs"
                        headers = {
                            "Content-Type": "application/json",
                            "Authorization": f"Bearer {tk}",
                            "x-aspose-client": "Containerize.Swagger"
                        }
                        response = requests.put(url, headers=headers, timeout=30)
                        response.raise_for_status()
                        print("Copied successful!")

                        for i in range(4):
                            pn = i
                            if pn < 2:
                                pn = 1
                            url = f"https://api.aspose.cloud/v3.0/pdf/{n}.pdf/pages/{pn}/text"
                            headers = {
                                "Content-Type": "application/json",
                                "Authorization": f"Bearer {tk}",
                                "x-aspose-client": "Containerize.Swagger"
                            }
                            response = requests.put(
                                url, headers=headers, json=datak[i], timeout=60)
                            response.raise_for_status()
                            print("Request successful!")
                        break
                except IndexError:
                    indexEr = True
                    break
                except requests.exceptions.Timeout:
                    w1.warning("Your session expired try again!")
                    downpdf = False
                    break
                except requests.exceptions.HTTPError as e:
                    print("Exception", e)
                    with open(r"cur.dat", "rb") as fp:
                        k = pickle.load(fp)
                        fk = open(r"cur.dat", "wb")
                        if k["month"] == datetime.datetime.now().month:
                            idn += 1
                            k["idn"] = k["idn"]+1
                            pickle.dump(k, fk)
                        else:
                            idn = 0
                            k["idn"] = k["idn"]+1
                            k["month"] = datetime.datetime.now().month
                            pickle.dump(k, fk)
                        fk.close()
            if indexEr:
                raise IndexError

            if downpdf:
                url = f"https://api.aspose.cloud/v3.0/pdf/storage/file/{n}.pdf"
                headers = {
                    "Content-Type": "accept: multipart/form-data",
                    "Authorization": f"Bearer {tk}"
                }
                # Add a timeout and stream the response to handle large files
                response = requests.get(url, headers=headers, timeout=60)
                time.sleep(2)
                with open(f"pdfs/{n}.pdf", "wb") as file:
                    file.write(response.content)

                l1.success("All Done!")

                with open(f"pdfs/{n}.pdf", "rb") as f:
                    b1.download_button("Download pdf", f, f"{n}.pdf", "application/pdf")

        except Exception as e:
            os.write(1, f"Exception 2 {e}".encode())
            l1.error("AN ERROR OCCURED! Please contact Sujal")
    else:
        w1.warning("PLEASE ENTER YOUR NAME OR TOPIC BEFORE CONTINUING!")


st.title("Certificate Generator")
st.caption("By Sujal❤️")

#h=st.header("UNDER SOME WORK PLEASE VIST AFTRR SOME TIME")

name = st.text_input("Enter Your Name")

col1, col2, col3 = st.columns(3)

sub = col1.selectbox("Select the subject", [
                     "Chemistry", "English", "Physics", "Biology", "Physical Education"])
cls = col2.selectbox("Select the class", ["IX", "X", "XI", "XII"])
sec = col3.selectbox("Select the section", ["A", "B", "C", "D"])

topic = st.empty()
inp = topic.text_input("Enter your topic")

w1 = st.empty()

radio = st.radio("Your Pronouns", ['He/his', 'She/her'])

b1 = st.empty()

if name=="":
    c1 = b1.button("Done", disabled=True)
elif (name=="" or inp=="") and sub!="English" and sub!="Physical Education":
    c1 = b1.button("Done", disabled=True)
else:
    c1 = b1.button("Done", disabled=False)

l1 = st.empty()

st.caption('If you got any errors please contact me:)')

if sub == "English" or sub == "Physical Education":
    topic.empty()
    #w1.warning("The English pdf will be available after 5pm today because of some ongoing change")

if len(inp) > 80:
    w1.warning("Your topic is way too big!😢 Please make it shorter else there will be layout problems")
    
if c1 and name and sub=="English":
    b1.empty()
    l1.success("Processing Please Wait")
    designs(sub, name, cls, sec, radio,
            "LOST SPRING :- REFLECTION OF CHILD LABOUR IN INDIA")

if c1 and name and sub=="Physical Education":
    b1.empty()
    l1.success("Processing Please Wait")
    designs(sub, name, cls, sec, radio,
            "PHYSICAL FITNESS, YOGAIC PRACTICE AND PROFICIENCY IN GAMES")

if c1 and name and inp and sub!="English" and sub!="Physical Education":
    b1.empty()
    l1.success("Processing Please Wait")
    designs(sub, name, cls, sec, radio, inp)

if c1 and not name:
    w1.warning("Please enter your name before continuing!")

if  c1 and not inp and sub!="English" and sub!="Physical Education":
    w1.warning("Please enter your topic before continuing!")