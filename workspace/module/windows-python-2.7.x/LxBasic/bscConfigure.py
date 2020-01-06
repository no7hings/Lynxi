# coding:utf-8


class HtmlColor(object):
    def __init__(self):
        self.cls_colorLis = [
            u'#ff003f',  # 0 (255, 0, 63)
            u'#fffd3f',  # 1 (255, 255, 63)
            u'#ff7f3f',  # 2 (255, 127, 63)
            u'#3fff7f',  # 3 (64, 255, 127)
            u'#3f7fff',  # 4 (63, 127, 255)

            u'#dfdfdf',  # 5 (223, 223, 223)
            u'#dfdfdf',  # 6 (191, 191, 191)
            u'#7f7f7f',  # 7 (127, 127, 127)
            u'#3f3f3f',  # 8 (63, 63, 63)
            u'#1f1f1f'   # 9 (31, 31, 31)
        ]

    @property
    def red(self):
        return self.cls_colorLis[0]

    @property
    def yellow(self):
        return self.cls_colorLis[1]

    @property
    def orange(self):
        return self.cls_colorLis[2]

    @property
    def green(self):
        return self.cls_colorLis[3]

    @property
    def blue(self):
        return self.cls_colorLis[4]

    @property
    def white(self):
        return self.cls_colorLis[5]

    @property
    def gray(self):
        return self.cls_colorLis[7]

    @property
    def black(self):
        return self.cls_colorLis[9]

    def raw(self):
        return self.cls_colorLis


class HsvColor(object):
    def __init__(self):
        pass


class Ui(object):
    @property
    def families(self):
        """
        :return: list
        """
        return [
            u'Arial',
            u'Arial Unicode MS',
            u'Arial Black'
        ]

    @property
    def htmlColors(self):
        """
        * 0 ( 255, 0, 64 ), 1 (255, 255, 64), 2 (255, 127, 0), 3 (64, 255, 127), 4 (0, 223, 223),
        * 5 (191, 191, 191), 6 (223, 223, 223), 7 (127, 127, 127), 8 (0, 0, 0)
        :return: list
        """
        return HtmlColor().raw()
