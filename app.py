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

ci = ['f00ee90c-844e-429b-b0d8-e83b6b0f8485', '5942cc6e-8a9a-43e1-b08b-b6086b662d3e', 'a0b2bbc8-7bbc-4ff6-8297-bcf0274a59f7', 'acc0a85d-1da2-4e81-952f-1733aba6f6da', '31fd9e38-da94-4abe-9bd3-be994f2f3eb1', '73f05917-83b4-47ea-9f8e-b52cdc369f75', '3ca53c5f-7e04-4b30-9771-1f4c56e1486d', 'a34b103f-51bc-4dd0-a4af-f2ad389c6f5c', '2b7cb818-2538-4290-b3d4-c58ee7e6c207', 'd6f78a8a-5b71-43d9-98d0-39cddb82e2a2', 'e4f92bf6-13a8-4b16-9538-fe5bd19d137f', '82865ebc-5315-4b1b-a716-8bb1d0b1fdce', '55f26a6b-3e1b-4bcf-a9c1-2147e6884200', '48091455-2ab2-42db-ade6-6b628cf992f1', '25df754a-b4c7-4836-b188-7ff8c0a6f58c', '8e07c94a-843d-4050-95f7-ff83bcc1c891', 'f3c3b3cc-a44e-4f37-bc38-25cf1de6c15a', '31d15410-d02c-4184-aa1c-76535d38b6b4', 'f15908a9-ff66-453e-81d0-a7cc8c63c039']
cs = ['22ba986cc956b6b4fd2b75b818c5c83f', 'ae9b39c64b73e72ab8d7dad8b036213a', '9325c76d2e4335071c97219bc105181a', '54a726f034e76edbfc5748d2548eab8c', '33b434f56b041bf6a8276af805bb73bb', '87fbdf770caf7daf439e824c17bfd3a7', '3115daff089a9c33dcab910eca19a86b', '848ec34b02ee0fa40fd77a74ebcc9c73', 'c5c4c907263cb1ff79062d20dc99c5a0', '38591d60eb8e7c407c610c82a87f4d10', 'a6feb8e0782e5f7fb0fc2da57940312e', '6f083c1a83f5b3ca0c5eab2df95929a9', '5292223022389d951eafb09245ca3c3a', 'bc55be74d4ed10440e2f93fc768719e4', '8fbdf6c7cdbb32fe32e57409f708198b', 'c460ca6b13694b4c6569adacc3ca12d0', '642a08be16e482424f91e7cc988a9b9c', '63850efcb987e0c11c2b8064d5b87b49', 'cca5cfc06ecf9f598e8320b0971dee3d']

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

        if r[4]:
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
    global idn, b1, l1

    try:
        datak = genTuple(subject, name, cls, sec, pron, topic)

        n = (name.replace(' ', '')).lower()

        indexEr = False

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
            except Exception as e:
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
        #l1.error("proble", e)
        l1.error("AN ERROR OCCURED! Please contact Sujal")


st.title("Certificate Generator")
st.caption("By Sujal❤️")

name = st.text_input("Enter Your Name")

col1, col2, col3 = st.columns(3)

sub = col1.selectbox("Select the subject", [
                     "English", "Chemistry", "Physics", "Biology"])
cls = col2.selectbox("Select the class", ["IX", "X", "XI", "XII"])
sec = col3.selectbox("Select the section", ["A", "B", "C", "D"])

topic = st.empty()
inp = topic.text_input("Enter your topic")

w1 = st.empty()

radio = st.radio("Your Pronouns", ['He/his', 'She/her'])

b1 = st.empty()
c1 = b1.button("Done")

l1 = st.empty()

st.caption('If you got any errors please contact me:)')

if sub == "English":
    topic.empty()

if len(inp) > 60:
    w1.warning("Your topic is way too big!😢 Please make it shorter else there will be layout problems")
    
if c1:
    b1.empty()
    l1.success("Processing Please Wait")
    if sub == "English":
        designs(sub, name, cls, sec, radio,
                "LOST SPRING :- REFLECTION OF CHILD LABOUR IN INDIA")
    else:
        designs(sub, name, cls, sec, radio, inp)
