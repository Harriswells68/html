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

ci = ['b439e6c2-4439-4419-9ac4-07afc94f583c', '431d4059-622e-4545-8058-2de6a143dab5', '4519794d-e1a6-438b-8ac1-cf3047ab50b9', 'e2d2bcd5-cc64-48a5-abc4-f4fc220a4fa6', '3b481882-ba10-4eef-a1b8-c51f3c759385', '2ebcaf4c-88e1-4466-b1d3-e4da35774c42', 'fffeada1-5767-4b64-af9b-6aaca5673c7a', '8225b6b0-c9a9-4bb3-baa4-3d85f9b4b525', '327c8776-ae6a-4f51-88d1-8576870120d5', '2613ee6d-751f-4e0b-bc78-ec2ef50c9111', 'ee8c88d7-173f-41c3-962b-2bde8bc4b780', '2484bd09-0f7f-491c-842a-bef50c0931a9', '599f783b-4356-46d6-abbc-99d4a0d897e7', 'fc394665-09ba-4e7b-aaa6-3a144b22ee98', '76a3273a-23b1-4e9b-8598-baae0d311659', '57b939ad-11a5-45a2-ba9e-5979a4e92c87', '1d42082e-cd25-4feb-8825-59d8c4e167bb', '5b6fc3c8-14c7-4a61-83fd-ffe44c70bd90', 'b2bc4c41-a738-44cc-b2c6-0842b5c1712c', 'a3a25445-e964-4698-bab5-7aa83845125f']
cs = ['43b39ddd5c01b95768aaaa2f605ee537', '56c17d9601ba521b3359bee30d3eada9', '4cb7c73cdd1a0912fa3fe920964c7886', '7c7a3dac8fb871a8c752caa5b49020a3', '99311c55b72bc66683c5f227bc0cfc4d', 'd9bb6fcc883c5e99518f1e3ada7e1342', '75fb4e07b4e9d6dff294610481022fcd', 'f1e84547ba8bb50f0e3f2a76be6b955a', '6b0745c198c8fbe9865b60c1f931ba41', 'b55d089a07f08cab35e8686a2883c292', 'f4949f34bbdd63a98889f9df126ba852', '4a3c8c1481d977acc430a8247b0e1a2f', 'c5a36032351a69064283e166131f9583', '23678f67fc7a63face9897b5a85e213e', 'ebfcf8884868da3fc3a20de3cb366cdb', 'd0ae3b534c6c0c8edd7b58e7b10dfd18', '7a6625c30510fb9df26c04dfdb0f3b04', 'ec640962a9f3ea2bf3c1a4955a754483', '7f2e21175bf5b7410beb816ac505c596', 'f37f1f5c01699357c7d1e808a295322f']

def checkOverflow(name, topic=None):
    name = name.upper()

    b1 = len(name) > 21
    b2 = len(topic) > 25
    b3 = len(topic) > 40

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
        return (name, topic, b1, b2, b3)

    elif len(topic) > 25:
        return (name, topic, b1, b2, b3)


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

        return (nameconfig, topicconfig, certconfig, acknconfig)

    except Exception as e:
        print(e)
        return None


def designs(subject, name, cls, sec, pron, topic):
    global idn, b1, l1, w1

    if name!="":

        try:
            datak = genTuple(subject, name, cls, sec, pron, topic)

            n = ((name.replace(' ', '')).lower()+subject.lower())

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

                    else:
                        url = f"https://api.aspose.cloud/v3.0/pdf/storage/file/copy/{subject.lower()}.pdf?destPath={n}.pdf&srcStorageName=pdfs&destStorageName=pdfs"
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
        w1.warning("PLEASE ENTER YOUR NAME BEFORE CONTINUING!")


st.title("Certificate Generator")
st.caption("By Sujal❤️")

#h=st.header("UNDER SOME WORK PLEASE VIST AFTRR SOME TIME")

name = st.text_input("Enter Your Name")

col1, col2, col3 = st.columns(3)

sub = col1.selectbox("Select the subject", [
                     "Chemistry", "English", "Physics", "Biology"])
cls = col2.selectbox("Select the class", ["IX", "X", "XI", "XII"])
sec = col3.selectbox("Select the section", ["A", "B", "C", "D"])

topic = st.empty()
inp = topic.text_input("Enter your topic")

w1 = st.empty()

radio = st.radio("Your Pronouns", ['He/his', 'She/her'])

b1 = st.empty()

if name=="":
    c1 = b1.button("Done", disabled=True)
else:
    c1 = b1.button("Done", disabled=False)

l1 = st.empty()

st.caption('If you got any errors please contact me:)')

if sub == "English":
    topic.empty()
    #w1.warning("The English pdf will be available after 5pm today because of some ongoing change")

if len(inp) > 60:
    w1.warning("Your topic is way too big!😢 Please make it shorter else there will be layout problems")
    
if c1 and name:
    b1.empty()
    l1.success("Processing Please Wait")
    if sub == "English":
        designs(sub, name, cls, sec, radio,
                "LOST SPRING :- REFLECTION OF CHILD LABOUR IN INDIA")
    else:
        designs(sub, name, cls, sec, radio, inp)

if c1 and not name:
    w1.warning("Please enter your name before continuing!")