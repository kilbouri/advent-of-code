class Ticket:

    _fieldRanges = {}

    def __init__(self) -> None:
        pass

    def getFields(self) -> set:
        return self._fieldRanges.keys()

    def addFieldRange(self, label: str, ranges: list[str]) -> None:
        existingRanges = self._fieldRanges.get(label, [])

        for r in ranges:
            minVal, maxVal = r.strip().split("-")
            existingRanges.append((int(minVal), int(maxVal)))

        self._fieldRanges[label] = existingRanges

    def isValidForField(self, field: str, value: int) -> bool:
        fieldRanges = self._fieldRanges.get(field, [])
        for r in fieldRanges:
            if r[0] <= value <= r[1]:
                return True

        return False

    def isValidValue(self, value: int) -> str:
        for label in self.getFields():
            if (self.isValidForField(label, value)):
                return label

        return ""
