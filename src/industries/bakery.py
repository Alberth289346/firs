from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(id='bakery',
                            accept_cargo_types=['BAKE', 'SUGR'],
                            prod_cargo_types=[],
                            prob_in_game='12',
                            prob_random='24',
                            prod_multiplier='[0, 0]',
                            map_colour='168',
                            life_type='IND_LIFE_TYPE_BLACK_HOLE',
                            spec_flags='bitmask(IND_FLAG_ONLY_IN_TOWNS)',
                            location_checks=dict(same_type_distance=16),
                            prospect_chance='0.75',
                            name='string(STR_IND_BAKERY)',
                            nearby_station_name='string(STR_STATION_TOWN_3)',
                            fund_cost_multiplier='15')

industry.economy_variations['EXTREME'].enabled = True

industry.add_tile(id='bakery_tile_1',
                  location_checks=TileLocationChecks(require_road_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='slab',
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 48, -31, -18)]
)
industry.add_spritelayout(
    id='bakery_spritelayout',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1]
)
industry.add_industry_layout(
    id='bakery_industry_layout',
    layout=[(0, 0, 'bakery_tile_1', 'bakery_spritelayout')]
)
