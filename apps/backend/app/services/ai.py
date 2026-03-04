
def infer_document_tags(filename: str, mime_type: str) -> dict:
    name = filename.lower()
    tagset = []
    if "invoice" in name:
        tagset.append("finance")
    if "passport" in name:
        tagset.append("identity")
    if mime_type == "application/pdf":
        tagset.append("pdf")
    return {"tags": tagset, "confidence": 0.84}


def summarize_document_text(text: str) -> str:
    return text[:200] + "..." if len(text) > 200 else text
