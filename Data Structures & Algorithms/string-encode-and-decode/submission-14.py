
class Solution:
    separator = "#"

    def encode(self, strs: List[str]) -> str:
        words = ""
        lengths = ""

        for word in strs:
            lengths += f"{len(word)},"
            words += word

        return lengths + self.separator + words

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        lengths, words = s.split(self.separator, 1)

        len_array = [
            int(length)
            for length in lengths.split(",")
            if length != ""
        ]
        

        final_array = []
        current_index = 0

        for length in len_array:
            final_array.append(
                words[current_index:current_index + length]
            )
            current_index += length

        return final_array
