from xml.dom.minidom import Document

__version__ = '0.1'
version = __version__


def searchIfChildNodeExist(nodeToCheck, nodeName):
    for childnote in nodeToCheck.childNodes:
        if childnote.nodeName == nodeName:
            return {"exists": True, "node": childnote}
    return {"exists": False, "node": None}


def writeTextNode(doc, nodeToAppendTo, dictPart):
    tempNode = None
    # prüfen ob ein @ enthalten
    for k, v in dictPart.items():
        if "@" in k:
            attrName = k.split("@")[1]
            tmpNodeName = k.split("@")[0]
            # schauen ob schon ein Node mit dem Namen vorhanden ist
            if searchIfChildNodeExist(nodeToAppendTo, tmpNodeName)["exists"] == True:
                tempNode = searchIfChildNodeExist(
                    nodeToAppendTo, tmpNodeName)["node"]
                tempNode.setAttribute(attrName, v)
            else:
                # als neuen Node ergänzen
                tempNode = doc.createElement(tmpNodeName)
                tempNode.setAttribute(attrName, v)
                nodeToAppendTo.appendChild(tempNode)
        else:
            tempNode = doc.createElement(k)
            tempNode.appendChild(doc.createTextNode(v))
            nodeToAppendTo.appendChild(tempNode)


def writeDictNode(doc, nodeToAppendTo, dictPart, nodeElementName):
    tmpNode = doc.createElement(nodeElementName)
    nodeToAppendTo.appendChild(tmpNode)
    for k, v in dictPart.items():
        if isinstance(v, list):
            pass
        elif isinstance(v, dict):
            writeDictNode(doc, tmpNode, v, k)
        else:
            writeTextNode(doc, tmpNode, {k: v})


def writeListNode(doc, nodeToAppendTo, dictPart, nodeElementName):
    tmpNode = doc.createElement(nodeElementName)
    nodeToAppendTo.appendChild(tmpNode)
    # es können nur noch Texte oder Dictionary kommen
    for listElement in dictPart:
        for k, v in listElement.items():
            if isinstance(v, dict):
                writeDictNode(doc, tmpNode, v, k)
            else:
                writeTextNode(doc, tmpNode, {k: v})


def convertDict2XML(pyDict,
                    rootNodeName):
    """
    Parameter:
    pyDict = dictionary to Convert
    rootNodeName = Name of the root-Node
    Converts a Dictionary to a minidom XML
    """

    doc = Document()

    # RootNode anlegen
    rootNode = doc.createElement(rootNodeName)
    doc.appendChild(rootNode)

    for k, v in pyDict.items():
        if isinstance(v, list):
            writeListNode(doc, rootNode, v, k)
        elif isinstance(v, dict):
            writeDictNode(doc, rootNode, v, k)
        else:
            writeTextNode(doc, rootNode, {k: v})

    return doc


if __name__ == "__main__":

    testNachricht2 = {
        "key1": "value1",
        "key2": "value2",
        "Adressat": {
            "Strasse": "Musterstraße",
            "HNR": "15",
            "Sonderinfos": {
                "bemerkung": "keine Bemerkung"
            }
        },
        "key1@name": "wert",
        "key1@name2": "wert2",
        "Akten": [{
            "Akte": {
                "Metadaten": {
                    "Betreff": "Test"
                },
                "Datum": "01.01.2021"
            }
        },
            {
            "Akte": {
                "Metadaten": {
                    "Betreff": "Test2",
                    "Betreff@xmlns": "abcde"
                },
                "Datum": "01.01.2021"
            }
        }
        ]
    }

    f = open("test.xml", "wb")
    f.write(convertDict2XML(testNachricht2,
                            "Nachricht").toprettyxml(encoding="UTF-8"))
    f.close()
