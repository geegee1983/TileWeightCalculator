# TM112_19J_TMA02_Q4_D2342461.py


def total_weight(width_tile, length_tile, number_of_tiles):
    """Given the dimensions of a tile (width and length in cm) and the number of tiles ordered, calculate total weight of the tiles that have been ordered."""
   
    one_tile_surface = width_tile * length_tile
    tile_surface = one_tile_surface * number_of_tiles
    total_weight = tile_surface * 10
    print(total_weight)
        
def test_total_weight():
    """Test the total_weight() function."""
    # Test for tile with dimensions 20, 20 and 
    # order of 30 tiles
    assert total_weight(20, 20, 30) == 120000
    
    # Test for tile with dimensions 1, 1 and 
    # order of 1 tile
    assert total_weight(1, 1, 1) == 10
    
    # Test for tile with dimensions 10, 0 and 
    # order of 10 tiles
    assert total_weight(10, 0, 10) == 0

    # Test for tile with dimensions 0, 10 and 
    # order of 15 tiles
    assert total_weight(0, 10, 15) == 0
    
    # Test for brick with dimensions 1, 1 and 
    # order of 0 tiles
    assert total_weight(1, 1, 0) == 0
    
    print ("tests passed") 
 
 
test_total_weight()
    
