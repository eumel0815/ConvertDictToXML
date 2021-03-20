# ConvertDictToXML
Python Library to Convert Dictionary to XML-Minidom

# Usage
You can simply use the Function "convertDict2XML" to convert your Python Dictionary to a minidom XML Document

```python
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
```

You can also specify XML Attributes in the following Syntax
```python
attribut = {"key1@name": "wert"}
```
The Code searches for an XML-Element with the name "key1" and adds the Attribut. If the Element does not exist it creates the Element with the Attribute.
