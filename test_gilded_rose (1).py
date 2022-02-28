from gilded_rose import Item, GildedRose


def test_item_criado_deve_ter_manter_propriedades_passadas():
    item = Item('objeto', 0, 0)
    assert [item.name, item.sell_in, item.quality] == ['objeto', 0, 0]


def test_queijo_brie_deve_aumentar_qualidade_quando_envelhece():
    queijo = Item('Aged Brie', 3, 3)
    gilded_queijo = GildedRose([queijo])
    gilded_queijo.update_quality()
    assert [queijo.sell_in, queijo.quality] == [2, 4]


def test_itens_normais_perdem_qualidade_quando_envelhecem():
    bolacha = Item('Bolacha', 3, 3)
    gilded_bolacha = GildedRose([bolacha])
    gilded_bolacha.update_quality()
    assert [bolacha.sell_in, bolacha.quality] == [2, 2]


def test_itens_normais_degradam_duas_vezes_mais_rapido_se_passar_do_tempo_de_venda():
    bolacha = Item('Bolacha', 0, 3)
    gilded_bolacha = GildedRose([bolacha])
    gilded_bolacha.update_quality()
    assert [bolacha.sell_in, bolacha.quality] == [-1, 1]


def test_itens_normais_nao_tem_qualidade_negativa():
    bolacha = Item('Bolacha', 3, 0)
    gilded_bolacha = GildedRose([bolacha])
    gilded_bolacha.update_quality()
    assert bolacha.quality >= 0


def test_a_qualidade_nao_deve_ser_maior_que_50():
    itens = [Item('Aged Brie', 3, 50), Item(
        'Backstage passes to a TAFKAL80ETC concert', 8, 50)]
    gilded_itens = GildedRose(itens)
    gilded_itens.update_quality()
    assert [itens[0].quality, itens[1].quality] == [50, 50]


def test_sulfuras_tem_qualidade_de_80():
    sulfuras = Item('Sulfuras, Hand of Ragnaros', 20, 80)
    gilded_sulfuras = GildedRose([sulfuras])
    gilded_sulfuras.update_quality()
    assert sulfuras.quality == 80


def test_sulfuras_tem_qualidade_de_80_mesmo_se_passar_do_tempo_de_venda():
    sulfuras = Item('Sulfuras, Hand of Ragnaros', 0, 80)
    gilded_sulfuras = GildedRose([sulfuras])
    gilded_sulfuras.update_quality()
    assert sulfuras.quality == 80


def test_entrada_aumenta_qualidade_em_1_com_mais_de_10_dias_para_venda():
    entrada = Item('Backstage passes to a TAFKAL80ETC concert', 12, 6)
    gilded_entrada = GildedRose([entrada])
    gilded_entrada.update_quality()
    assert [entrada.sell_in, entrada.quality] == [11, 7]


def test_entrada_aumenta_qualidade_em_2_com_menos_de_10_dias_para_venda():
    entrada = Item('Backstage passes to a TAFKAL80ETC concert', 8, 6)
    gilded_entrada = GildedRose([entrada])
    gilded_entrada.update_quality()
    assert [entrada.sell_in, entrada.quality] == [7, 8]


def test_entrada_aumenta_qualidade_em_3_com_menos_de_5_dias_para_venda():
    entrada = Item('Backstage passes to a TAFKAL80ETC concert', 2, 6)
    gilded_entrada = GildedRose([entrada])
    gilded_entrada.update_quality()
    assert [entrada.sell_in, entrada.quality] == [1, 9]

def test_entrada_aumenta_qualidade_em_3_com_menos_de_5_dias_para_venda_e_nao_passar_de_50():
    entrada = Item('Backstage passes to a TAFKAL80ETC concert', 2, 49)
    gilded_entrada = GildedRose([entrada])
    gilded_entrada.update_quality()
    assert [entrada.sell_in, entrada.quality] == [1, 50]


def test_entrada_zera_qualidade_passando_da_data_de_venda():
    entrada = Item('Backstage passes to a TAFKAL80ETC concert', 0, 6)
    gilded_entrada = GildedRose([entrada])
    gilded_entrada.update_quality()
    assert [entrada.sell_in, entrada.quality] == [-1, 0]


def test_itens_conjurados_perdem_qualidade_duas_vezes_mais_rapido():
    conjurado = Item('Conjured Mana Cake', 5, 6)
    conjurado_vencido = Item('Conjured Rat Soup', -1, 6)
    gilded_conjurados = GildedRose([conjurado, conjurado_vencido])
    gilded_conjurados.update_quality()
    assert [conjurado.quality, conjurado_vencido.quality] == [4, 2]
