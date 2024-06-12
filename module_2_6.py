def single_root_words(root_world, *other_world):
    same_world = []
    for world in other_world:
        if root_world.upper() in world.upper() or world.upper() in root_world.upper():
            same_world.append(world.upper())
    return same_world

spisok_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
spisok = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(spisok_1)
print(spisok)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies', 'Disablement',
                  'Able', 'Mable', 'Disable', 'Bagel')