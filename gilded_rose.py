# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality_brie(item):
        if item.quality < 50:
            item.quality += 1

    def update_quality_entrada(item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1

        item.quality = min(item.quality, 50)

    def update_quality_sulfuras(item):
        item.quality = 80

    def update_quality_normal(self, item):
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2

        item.quality = max(item.quality, 0)

    def update_quality_conjurado(self, item):
        if item.sell_in > 0:
            item.quality -= 2
        else:
            item.quality -= 4

        item.quality = max(item.quality, 0)

    itens_especiais = {
        'Aged Brie': update_quality_brie,
        'Backstage passes to a TAFKAL80ETC concert': update_quality_entrada,
        'Sulfuras, Hand of Ragnaros': update_quality_sulfuras,
    }

    def update_quality(self):
        for item in self.items:
            item.sell_in -= 1

            if item.name in self.itens_especiais.keys():
                self.itens_especiais[item.name](item)
            elif item.name.split()[0].capitalize() == 'Conjured':
                self.update_quality_conjurado(item)
            else:
                self.update_quality_normal(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
