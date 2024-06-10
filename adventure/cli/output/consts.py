from dataclasses import dataclass
from enum import Enum

type ColorTriplet = tuple[int, int, int]


@dataclass(slots=True, frozen=True, eq=True)
class Color:
    name: str
    number: int
    triplet: ColorTriplet

    def as_number(self) -> int:
        return self.number

    def as_name(self) -> str:
        return self.name

    def as_triplet(self) -> str:
        return self.triplet


class Colors(Enum):
    BLACK = Color("black", 0, (0, 0, 0))
    RED = Color("red", 1, (128, 0, 0))
    GREEN = Color("green", 2, (0, 128, 0))
    YELLOW = Color("yellow", 3, (128, 128, 0))
    BLUE = Color("blue", 4, (0, 0, 128))
    MAGENTA = Color("magenta", 5, (128, 0, 128))
    CYAN = Color("cyan", 6, (0, 128, 128))
    WHITE = Color("white", 7, (192, 192, 192))
    BRIGHT_BLACK = Color("bright_black", 8, (128, 128, 128))
    BRIGHT_RED = Color("bright_red", 9, (255, 0, 0))
    BRIGHT_GREEN = Color("bright_green", 10, (0, 255, 0))
    BRIGHT_YELLOW = Color("bright_yellow", 11, (255, 255, 0))
    BRIGHT_BLUE = Color("bright_blue", 12, (0, 0, 255))
    BRIGHT_MAGENTA = Color("bright_magenta", 13, (255, 0, 255))
    BRIGHT_CYAN = Color("bright_cyan", 14, (0, 255, 255))
    BRIGHT_WHITE = Color("bright_white", 15, (255, 255, 255))
    GREY0 = Color("grey0", 16, (0, 0, 0))
    NAVY_BLUE = Color("navy_blue", 17, (0, 0, 95))
    DARK_BLUE = Color("dark_blue", 18, (0, 0, 135))
    BLUE3 = Color("blue3", 20, (0, 0, 215))
    BLUE1 = Color("blue1", 21, (0, 0, 255))
    DARK_GREEN = Color("dark_green", 22, (0, 95, 0))

    DEEP_SKY_BLUE4 = Color("deep_sky_blue4", 25, (0, 95, 175))
    DODGER_BLUE3 = Color("dodger_blue3", 26, (0, 95, 215))
    DODGER_BLUE2 = Color("dodger_blue2", 27, (0, 95, 255))
    GREEN4 = Color("green4", 28, (0, 135, 0))
    SPRING_GREEN4 = Color("spring_green4", 29, (0, 135, 95))
    TURQUOISE4 = Color("turquoise4", 30, (0, 135, 135))
    DEEP_SKY_BLUE3 = Color("deep_sky_blue3", 32, (0, 135, 215))
    DODGER_BLUE1 = Color("dodger_blue1", 33, (0, 135, 255))
    GREEN3 = Color("green3", 40, (0, 215, 0))
    SPRING_GREEN3 = Color("spring_green3", 41, (0, 215, 95))
    DARK_CYAN = Color("dark_cyan", 36, (0, 175, 135))
    LIGHT_SEA_GREEN = Color("light_sea_green", 37, (0, 175, 175))
    DEEP_SKY_BLUE2 = Color("deep_sky_blue2", 38, (0, 175, 215))
    DEEP_SKY_BLUE1 = Color("deep_sky_blue1", 39, (0, 175, 255))
    SPRING_GREEN2 = Color("spring_green2", 47, (0, 255, 95))
    CYAN3 = Color("cyan3", 43, (0, 215, 175))
    DARK_TURQUOISE = Color("dark_turquoise", 44, (0, 215, 215))
    TURQUOISE2 = Color("turquoise2", 45, (0, 215, 255))
    GREEN1 = Color("green1", 46, (0, 255, 0))
    SPRING_GREEN1 = Color("spring_green1", 48, (0, 255, 135))
    MEDIUM_SPRING_GREEN = Color("medium_spring_green", 49, (0, 255, 175))
    CYAN2 = Color("cyan2", 50, (0, 255, 215))
    CYAN1 = Color("cyan1", 51, (0, 255, 255))
    DARK_RED = Color("dark_red", 88, (135, 0, 0))
    DEEP_PINK4 = Color("deep_pink4", 125, (175, 0, 95))
    PURPLE4 = Color("purple4", 55, (95, 0, 175))
    PURPLE3 = Color("purple3", 56, (95, 0, 215))
    BLUE_VIOLET = Color("blue_violet", 57, (95, 0, 255))
    ORANGE4 = Color("orange4", 94, (135, 95, 0))
    GREY37 = Color("grey37", 59, (95, 95, 95))
    MEDIUM_PURPLE4 = Color("medium_purple4", 60, (95, 95, 135))
    SLATE_BLUE3 = Color("slate_blue3", 62, (95, 95, 215))
    ROYAL_BLUE1 = Color("royal_blue1", 63, (95, 95, 255))
    CHARTREUSE4 = Color("chartreuse4", 64, (95, 135, 0))
    DARK_SEA_GREEN4 = Color("dark_sea_green4", 71, (95, 175, 95))
    PALE_TURQUOISE4 = Color("pale_turquoise4", 66, (95, 135, 135))
    STEEL_BLUE = Color("steel_blue", 67, (95, 135, 175))
    STEEL_BLUE3 = Color("steel_blue3", 68, (95, 135, 215))
    CORNFLOWER_BLUE = Color("cornflower_blue", 69, (95, 135, 255))
    CHARTREUSE3 = Color("chartreuse3", 76, (95, 215, 0))
    CADET_BLUE = Color("cadet_blue", 73, (95, 175, 175))
    SKY_BLUE3 = Color("sky_blue3", 74, (95, 175, 215))
    STEEL_BLUE1 = Color("steel_blue1", 81, (95, 215, 255))
    PALE_GREEN3 = Color("pale_green3", 114, (135, 215, 135))
    SEA_GREEN3 = Color("sea_green3", 78, (95, 215, 135))
    AQUAMARINE3 = Color("aquamarine3", 79, (95, 215, 175))
    MEDIUM_TURQUOISE = Color("medium_turquoise", 80, (95, 215, 215))
    CHARTREUSE2 = Color("chartreuse2", 112, (135, 215, 0))
    SEA_GREEN2 = Color("sea_green2", 83, (95, 255, 95))
    SEA_GREEN1 = Color("sea_green1", 85, (95, 255, 175))
    AQUAMARINE1 = Color("aquamarine1", 122, (135, 255, 215))
    DARK_MAGENTA = Color("dark_magenta", 91, (135, 0, 175))
    DARK_VIOLET = Color("dark_violet", 128, (175, 0, 215))
    PURPLE = Color("purple", 129, (175, 0, 255))
    LIGHT_PINK4 = Color("light_pink4", 95, (135, 95, 95))
    PLUM4 = Color("plum4", 96, (135, 95, 135))
    MEDIUM_PURPLE3 = Color("medium_purple3", 98, (135, 95, 215))
    SLATE_BLUE1 = Color("slate_blue1", 99, (135, 95, 255))
    YELLOW4 = Color("yellow4", 106, (135, 175, 0))
    WHEAT4 = Color("wheat4", 101, (135, 135, 95))
    GREY53 = Color("grey53", 102, (135, 135, 135))
    LIGHT_SLATE_GREY = Color("light_slate_grey", 103, (135, 135, 175))
    MEDIUM_PURPLE = Color("medium_purple", 104, (135, 135, 215))
    LIGHT_SLATE_BLUE = Color("light_slate_blue", 105, (135, 135, 255))
    DARK_OLIVE_GREEN3 = Color("dark_olive_green3", 149, (175, 215, 95))
    DARK_SEA_GREEN = Color("dark_sea_green", 108, (135, 175, 135))
    LIGHT_SKY_BLUE3 = Color("light_sky_blue3", 110, (135, 175, 215))
    SKY_BLUE2 = Color("sky_blue2", 111, (135, 175, 255))
    DARK_SEA_GREEN3 = Color("dark_sea_green3", 150, (175, 215, 135))
    SKY_BLUE1 = Color("sky_blue1", 117, (135, 215, 255))
    CHARTREUSE1 = Color("chartreuse1", 118, (135, 255, 0))
    LIGHT_GREEN = Color("light_green", 120, (135, 255, 135))
    PALE_GREEN1 = Color("pale_green1", 156, (175, 255, 135))
    RED3 = Color("red3", 160, (215, 0, 0))
    MEDIUM_VIOLET_RED = Color("medium_violet_red", 126, (175, 0, 135))
    MAGENTA3 = Color("magenta3", 164, (215, 0, 215))
    DARK_ORANGE3 = Color("dark_orange3", 166, (215, 95, 0))
    INDIAN_RED = Color("indian_red", 167, (215, 95, 95))
    HOT_PINK3 = Color("hot_pink3", 168, (215, 95, 135))
    MEDIUM_ORCHID3 = Color("medium_orchid3", 133, (175, 95, 175))
    MEDIUM_ORCHID = Color("medium_orchid", 134, (175, 95, 215))
    MEDIUM_PURPLE2 = Color("medium_purple2", 140, (175, 135, 215))
    DARK_GOLDENROD = Color("dark_goldenrod", 136, (175, 135, 0))
    LIGHT_SALMON3 = Color("light_salmon3", 173, (215, 135, 95))
    ROSY_BROWN = Color("rosy_brown", 138, (175, 135, 135))
    GREY63 = Color("grey63", 139, (175, 135, 175))
    MEDIUM_PURPLE1 = Color("medium_purple1", 141, (175, 135, 255))
    GOLD3 = Color("gold3", 178, (215, 175, 0))
    DARK_KHAKI = Color("dark_khaki", 143, (175, 175, 95))
    NAVAJO_WHITE3 = Color("navajo_white3", 144, (175, 175, 135))
    GREY69 = Color("grey69", 145, (175, 175, 175))
    LIGHT_STEEL_BLUE3 = Color("light_steel_blue3", 146, (175, 175, 215))
    LIGHT_STEEL_BLUE = Color("light_steel_blue", 147, (175, 175, 255))
    YELLOW3 = Color("yellow3", 184, (215, 215, 0))
    DARK_SEA_GREEN2 = Color("dark_sea_green2", 157, (175, 255, 175))
    LIGHT_CYAN3 = Color("light_cyan3", 152, (175, 215, 215))
    LIGHT_SKY_BLUE1 = Color("light_sky_blue1", 153, (175, 215, 255))
    GREEN_YELLOW = Color("green_yellow", 154, (175, 255, 0))
    DARK_OLIVE_GREEN2 = Color("dark_olive_green2", 155, (175, 255, 95))
    DARK_SEA_GREEN1 = Color("dark_sea_green1", 193, (215, 255, 175))
    PALE_TURQUOISE1 = Color("pale_turquoise1", 159, (175, 255, 255))
    DEEP_PINK3 = Color("deep_pink3", 162, (215, 0, 135))
    MAGENTA2 = Color("magenta2", 200, (255, 0, 215))
    HOT_PINK2 = Color("hot_pink2", 169, (215, 95, 175))
    ORCHID = Color("orchid", 170, (215, 95, 215))
    MEDIUM_ORCHID1 = Color("medium_orchid1", 207, (255, 95, 255))
    ORANGE3 = Color("orange3", 172, (215, 135, 0))
    LIGHT_PINK3 = Color("light_pink3", 174, (215, 135, 135))
    PINK3 = Color("pink3", 175, (215, 135, 175))
    PLUM3 = Color("plum3", 176, (215, 135, 215))
    VIOLET = Color("violet", 177, (215, 135, 255))
    LIGHT_GOLDENROD3 = Color("light_goldenrod3", 179, (215, 175, 95))
    TAN = Color("tan", 180, (215, 175, 135))
    MISTY_ROSE3 = Color("misty_rose3", 181, (215, 175, 175))
    THISTLE3 = Color("thistle3", 182, (215, 175, 215))
    PLUM2 = Color("plum2", 183, (215, 175, 255))
    KHAKI3 = Color("khaki3", 185, (215, 215, 95))
    LIGHT_GOLDENROD2 = Color("light_goldenrod2", 222, (255, 215, 135))
    LIGHT_YELLOW3 = Color("light_yellow3", 187, (215, 215, 175))
    GREY84 = Color("grey84", 188, (215, 215, 215))
    LIGHT_STEEL_BLUE1 = Color("light_steel_blue1", 189, (215, 215, 255))
    YELLOW2 = Color("yellow2", 190, (215, 255, 0))
    DARK_OLIVE_GREEN1 = Color("dark_olive_green1", 192, (215, 255, 135))
    HONEYDEW2 = Color("honeydew2", 194, (215, 255, 215))
    LIGHT_CYAN1 = Color("light_cyan1", 195, (215, 255, 255))
    RED1 = Color("red1", 196, (255, 0, 0))
    DEEP_PINK2 = Color("deep_pink2", 197, (255, 0, 95))
    DEEP_PINK1 = Color("deep_pink1", 199, (255, 0, 175))
    MAGENTA1 = Color("magenta1", 201, (255, 0, 255))
    ORANGE_RED1 = Color("orange_red1", 202, (255, 95, 0))
    INDIAN_RED1 = Color("indian_red1", 204, (255, 95, 135))
    HOT_PINK = Color("hot_pink", 206, (255, 95, 215))
    DARK_ORANGE = Color("dark_orange", 208, (255, 135, 0))
    SALMON1 = Color("salmon1", 209, (255, 135, 95))
    LIGHT_CORAL = Color("light_coral", 210, (255, 135, 135))
    PALE_VIOLET_RED1 = Color("pale_violet_red1", 211, (255, 135, 175))
    ORCHID2 = Color("orchid2", 212, (255, 135, 215))
    ORCHID1 = Color("orchid1", 213, (255, 135, 255))
    ORANGE1 = Color("orange1", 214, (255, 175, 0))
    SANDY_BROWN = Color("sandy_brown", 215, (255, 175, 95))
    LIGHT_SALMON1 = Color("light_salmon1", 216, (255, 175, 135))
    LIGHT_PINK1 = Color("light_pink1", 217, (255, 175, 175))
    PINK1 = Color("pink1", 218, (255, 175, 215))
    PLUM1 = Color("plum1", 219, (255, 175, 255))
    GOLD1 = Color("gold1", 220, (255, 215, 0))
    NAVAJO_WHITE1 = Color("navajo_white1", 223, (255, 215, 175))
    MISTY_ROSE1 = Color("misty_rose1", 224, (255, 215, 215))
    THISTLE1 = Color("thistle1", 225, (255, 215, 255))
    YELLOW1 = Color("yellow1", 226, (255, 255, 0))
    LIGHT_GOLDENROD1 = Color("light_goldenrod1", 227, (255, 255, 95))
    KHAKI1 = Color("khaki1", 228, (255, 255, 135))
    WHEAT1 = Color("wheat1", 229, (255, 255, 175))
    CORNSILK1 = Color("cornsilk1", 230, (255, 255, 215))
    GREY100 = Color("grey100", 231, (255, 255, 255))
    GREY3 = Color("grey3", 232, (8, 8, 8))
    GREY7 = Color("grey7", 233, (18, 18, 18))
    GREY11 = Color("grey11", 234, (28, 28, 28))
    GREY15 = Color("grey15", 235, (38, 38, 38))
    GREY19 = Color("grey19", 236, (48, 48, 48))
    GREY23 = Color("grey23", 237, (58, 58, 58))
    GREY27 = Color("grey27", 238, (68, 68, 68))
    GREY30 = Color("grey30", 239, (78, 78, 78))
    GREY35 = Color("grey35", 240, (88, 88, 88))
    GREY39 = Color("grey39", 241, (98, 98, 98))
    GREY42 = Color("grey42", 242, (108, 108, 108))
    GREY46 = Color("grey46", 243, (118, 118, 118))
    GREY50 = Color("grey50", 244, (128, 128, 128))
    GREY54 = Color("grey54", 245, (138, 138, 138))
    GREY58 = Color("grey58", 246, (148, 148, 148))
    GREY62 = Color("grey62", 247, (158, 158, 158))
    GREY66 = Color("grey66", 248, (168, 168, 168))
    GREY70 = Color("grey70", 249, (178, 178, 178))
    GREY74 = Color("grey74", 250, (188, 188, 188))
    GREY78 = Color("grey78", 251, (198, 198, 198))
    GREY82 = Color("grey82", 252, (208, 208, 208))
    GREY85 = Color("grey85", 253, (218, 218, 218))
    GREY89 = Color("grey89", 254, (228, 228, 228))
    GREY93 = Color("grey93", 255, (238, 238, 238))

    # unnamed colors
    COLOR19 = Color("", 19, (0, 0, 175))
    COLOR23 = Color("", 23, (0, 95, 95))
    COLOR24 = Color("", 24, (0, 95, 135))
    COLOR31 = Color("", 31, (0, 135, 175))
    COLOR34 = Color("", 34, (0, 175, 0))
    COLOR35 = Color("", 35, (0, 175, 95))
    COLOR42 = Color("", 42, (0, 215, 135))
    COLOR52 = Color("", 52, (95, 0, 0))
    COLOR53 = Color("", 53, (95, 0, 95))
    COLOR54 = Color("", 54, (95, 0, 135))
    COLOR58 = Color("", 58, (95, 95, 0))
    COLOR61 = Color("", 61, (95, 95, 175))
    COLOR65 = Color("", 65, (95, 135, 95))
    COLOR70 = Color("", 70, (95, 175, 0))
    COLOR72 = Color("", 72, (95, 175, 135))
    COLOR75 = Color("", 75, (95, 175, 255))
    COLOR77 = Color("", 77, (95, 215, 95))
    COLOR82 = Color("", 82, (95, 255, 0))
    COLOR84 = Color("", 84, (95, 255, 135))
    COLOR86 = Color("", 86, (95, 255, 215))
    COLOR87 = Color("", 87, (95, 255, 255))
    COLOR89 = Color("", 89, (135, 0, 95))
    COLOR90 = Color("", 90, (135, 0, 135))
    COLOR92 = Color("", 92, (135, 0, 215))
    COLOR93 = Color("", 93, (135, 0, 255))
    COLOR97 = Color("", 97, (135, 95, 175))
    COLOR100 = Color("", 100, (135, 135, 0))
    COLOR107 = Color("", 107, (135, 175, 95))
    COLOR109 = Color("", 109, (135, 175, 175))
    COLOR113 = Color("", 113, (135, 215, 95))
    COLOR115 = Color("", 115, (135, 215, 175))
    COLOR116 = Color("", 116, (135, 215, 215))
    COLOR119 = Color("", 119, (135, 255, 95))
    COLOR121 = Color("", 121, (135, 255, 175))
    COLOR123 = Color("", 123, (135, 255, 255))
    COLOR124 = Color("", 124, (175, 0, 0))
    COLOR127 = Color("", 127, (175, 0, 175))
    COLOR130 = Color("", 130, (175, 95, 0))
    COLOR131 = Color("", 131, (175, 95, 95))
    COLOR132 = Color("", 132, (175, 95, 135))
    COLOR135 = Color("", 135, (175, 95, 255))
    COLOR137 = Color("", 137, (175, 135, 95))
    COLOR142 = Color("", 142, (175, 175, 0))
    COLOR148 = Color("", 148, (175, 215, 0))
    COLOR151 = Color("", 151, (175, 215, 175))
    COLOR158 = Color("", 158, (175, 255, 215))
    COLOR161 = Color("", 161, (215, 0, 95))
    COLOR163 = Color("", 163, (215, 0, 175))
    COLOR165 = Color("", 165, (215, 0, 255))
    COLOR171 = Color("", 171, (215, 95, 255))
    COLOR186 = Color("", 186, (215, 215, 135))
    COLOR191 = Color("", 191, (215, 255, 95))
    COLOR198 = Color("", 198, (255, 0, 135))
    COLOR203 = Color("", 203, (255, 95, 95))
    COLOR205 = Color("", 205, (255, 95, 175))
    COLOR221 = Color("", 221, (255, 215, 95))

    @staticmethod
    def get_by_name(name: str) -> Color:
        for _color in Colors:
            if _color.value.name == name:
                return _color.value

        raise ValueError(f"invalid color name {name}")

    @staticmethod
    def get_by_number(number: int) -> Color:
        for _color in Colors:
            if _color.value.number == number:
                return _color.value

        raise ValueError(f"invalid color number {number}")

    @staticmethod
    def get_by_triplet(triplet: ColorTriplet) -> Color:
        for _color in Colors:
            if _color.value.triplet == triplet:
                return _color.value

        raise ValueError(f"invalid color triplet {triplet}")

    def as_color(self) -> Color:
        return self.value


for i in range(256):
    try:
        Colors.get_by_number(i)
    except ValueError:
        print(i)


[
    19,
    23,
    24,
    31,
    34,
    35,
    42,
    52,
    53,
    54,
    58,
    61,
    65,
    70,
    72,
    75,
    77,
    82,
    84,
    86,
    87,
    89,
    90,
    92,
    93,
    97,
    100,
    107,
    109,
    113,
    115,
    116,
    119,
    121,
    123,
    124,
    127,
    130,
    131,
    132,
    135,
    137,
    142,
    148,
    151,
    158,
    161,
    163,
    165,
    171,
    186,
    191,
    198,
    203,
    205,
    221,
]
