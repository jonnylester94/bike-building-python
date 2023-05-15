from main import *
from custom_exceptions import *
import pytest

# component class
@pytest.mark.component_class
def test_that_component_class_has_current_state_attribute():
    new_component = Component(0, 0)
    assert 'current_state' in dir(new_component)

@pytest.mark.component_class
def test_that_component_class_has_max_lifespan_attribute():
     new_component = Component(0, 0)
     assert 'max_lifespan' in dir(new_component)

@pytest.mark.component_class
def test_that_component_class_has_check_condition_method():
     new_component = Component(0, 0)
     assert 'check_condition' in dir(new_component)

@pytest.mark.component_class
def test_that_check_condition_method_returns_the_current_state():
     new_component = Component(68, 0)
     assert new_component.check_condition() == 68


# bell component
@pytest.mark.bell
def test_that_bell_child_class_has_a_warn_pedestrian_method():
     new_bell = Bell(60, 8)
     assert 'warn_pedestrian' in dir(new_bell)

@pytest.mark.bell
def test_that_warn_pedestrian_method_decreases_current_state_of_bell_by_correct_amount():
     new_bell = Bell(42, 8)
     new_bell.warn_pedestrian()
     assert new_bell.current_state == 29.5

@pytest.mark.bell
def test_that_warn_pedestrian_method_can_only_be_used_if_not_broken():
     new_bell = Bell(0, 8)
     new_bell.warn_pedestrian()
     assert new_bell.current_state == 0


# brakes component
@pytest.mark.brakes
def test_that_brakes_child_class_has_a_squeeze_brakes_method():
     new_brakes = Brakes(0, 0)
     assert 'squeeze_brakes' in dir(new_brakes)

@pytest.mark.brakes
def test_that_squeeze_brakes_method_decreases_current_state_of_brakes_by_correct_amount():
     new_brakes = Brakes(86, 12.5)
     new_brakes.squeeze_brakes()
     assert new_brakes.current_state == 78

@pytest.mark.brakes
def test_that_squeeze_brakes_method_can_only_be_used_if_not_broken():
     new_brakes = Brakes(0, 12.5)
     new_brakes.squeeze_brakes()     
     assert new_brakes.current_state == 0


# chain component
@pytest.mark.chain
def test_that_chain_child_class_has_a_propels_bike_method():
     new_chain = Chain(0, 0)
     assert 'propels_bike' in dir(new_chain)

@pytest.mark.chain
def test_that_propels_bike_method_decreases_current_state_of_chain_by_correct_amount():
     new_chain = Chain(2, 1)
     new_chain.propels_bike()
     assert new_chain.current_state == -98

@pytest.mark.chain
def test_that_propels_bike_method_can_only_be_used_if_not_broken():
     new_chain = Chain(0, 1)
     new_chain.propels_bike()
     assert new_chain.current_state == 0


# tyres component
@pytest.mark.tyres
def test_that_tyres_child_class_has_a_provides_grip_method():
     new_tyres = Tyres(0, 0)
     assert 'provides_grip' in dir(new_tyres)

@pytest.mark.tyres
def test_that_provides_grip_method_decreases_current_state_of_tyres_by_correct_amount():
     new_tyres = Tyres(59, 20)
     new_tyres.provides_grip()
     assert new_tyres.current_state == 54  

@pytest.mark.tyres
def test_that_provides_grip_method_can_only_be_used_if_not_broken():
     new_tyres = Tyres(0, 20)
     new_tyres.provides_grip()
     assert new_tyres.current_state == 0


# pedals component
@pytest.mark.pedals
def test_that_pedals_child_class_has_a_holds_foot_method():
     new_pedals = Pedals(0, 0)
     assert 'holds_foot' in dir(new_pedals)

@pytest.mark.pedals
def test_that_holds_foot_method_decreases_current_state_of_pedals_by_correct_amount():
     new_pedals = Pedals(31, 10)
     new_pedals.holds_foot()
     assert new_pedals.current_state == 21

@pytest.mark.pedals
def test_that_holds_foot_method_can_only_be_used_if_not_broken():
     new_pedals = Pedals(0, 10)
     new_pedals.holds_foot()
     assert new_pedals.current_state == 0


# bikes
@pytest.mark.bikes
def test_that_bike_ride_method_can_be_used_if_all_components_are_not_broken():
    new_bell = Bell(47,8)
    new_brakes = Brakes(85,12.5)
    new_chain = Chain(32,1)
    new_tyres = Tyres(20,20)
    new_pedals = Pedals(67,10)
    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
    assert 'ride' in dir(new_bike)

@pytest.mark.bikes
def test_that_using_bike_ride_method_decreases_the_current_state_of_each_component_by_correct_amount():
    new_bell = Bell(47,8)
    new_brakes = Brakes(85,12.5)
    new_chain = Chain(32,1)
    new_tyres = Tyres(20,20)
    new_pedals = Pedals(67,10)
    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
    new_bike.ride()
    assert new_bike.bell.current_state == 34.5
    assert new_bike.brakes.current_state == 77
    assert new_bike.chain.current_state == -68
    assert new_bike.tyres.current_state == 15
    assert new_bike.pedals.current_state == 57

@pytest.mark.bikes
def test_that_if_all_components_are_good_or_pristine_this_returns_a_print_statement_saying_the_ride_was_excellent():
    new_bell = Bell(88,8)
    new_brakes = Brakes(85,12.5)
    new_chain = Chain(92,5)
    new_tyres = Tyres(98,20)
    new_pedals = Pedals(67,10)
    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
    result = new_bike.ride()
    expected = 'What an excellent ride!'
    assert new_bike.bell.current_state == 75.5
    assert new_bike.brakes.current_state == 77
    assert new_bike.chain.current_state == 72
    assert new_bike.tyres.current_state == 93
    assert new_bike.pedals.current_state == 57
    assert result == expected

@pytest.mark.bikes
def test_that_if_any_component_is_fragile_but_none_are_broken_should_return_a_print_statement_saying_a_great_ride_but_part_of_me_is_about_to_break():
    new_bell = Bell(88,8)
    new_brakes = Brakes(85,12.5)
    new_chain = Chain(92,5)
    new_tyres = Tyres(98,20)
    new_pedals = Pedals(22, 10)
    new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
    result = new_bike.ride()
    expected = 'A great ride but part of me is about to break!'
    assert new_bike.bell.current_state == 75.5
    assert new_bike.brakes.current_state == 77
    assert new_bike.chain.current_state == 72
    assert new_bike.tyres.current_state == 93
    assert new_bike.pedals.current_state == 12
    assert result == expected

@pytest.mark.bikes
def test_that_ring_bell_method_returns_ring_ring_ring_print_statement_if_all_parts_are_good_or_pristine():
     new_bell = Bell(88,8)
     new_brakes = Brakes(85,12.5)
     new_chain = Chain(92,5)
     # print(new_chain.__dict__)
     new_tyres = Tyres(98,20)
     new_pedals = Pedals(52,10)
     new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
     # print(new_bike.pedals.__dict__)
     result = new_bike.ring_bell()
     expected = 'Ring! Ring! Ring!'
     assert result == expected

@pytest.mark.bikes
def test_that_ring_bell_method_returns_bell_fell_off_if_any_components_are_broken():
     new_bell = Bell(88,8)
     new_brakes = Brakes(0,12.5)
     new_chain = Chain(92,5)
     # print(new_chain.__dict__)
     new_tyres = Tyres(0,20)
     new_pedals = Pedals(52,10)
     new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
     # print(new_bike.pedals.__dict__)
     result = new_bike.ring_bell()
     expected = 'The bell fell off!'
     assert result == expected

@pytest.mark.bikes
def test_that_ring_bell_method_returns_ring_cling_if_any_components_are_fragile_but_none_are_broken():
     new_bell = Bell(18,8)
     # print(new_bell.__dict__)
     new_brakes = Brakes(33,12.5)
     new_chain = Chain(92,5)
     new_tyres = Tyres(98,20)
     new_pedals = Pedals(22,10)
     new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
     # print(new_bike.bell.__dict__)
     result = new_bike.ring_bell()
     expected = 'Ring! Cling...'
     assert result == expected

@pytest.mark.bikes
def test_that_ring_bell_method_otherwise_returns_I_am_in_mixed_condition_message():
     new_bell = Bell(88,8)
     new_brakes = Brakes(85,12.5)
     new_chain = Chain(92,5)
     new_tyres = Tyres(98,20)
     new_pedals = Pedals(44,10)
     new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
     result = new_bike.ring_bell()
     expected = 'I am in mixed condition!'
     assert result == expected
     

@pytest.mark.errors
def test_that_error_raised_when_current_state_passed_is_out_of_range():
     with pytest.raises(InvalidInput):
          Bell(150,12)

@pytest.mark.errors
def test_that_error_raised_when_current_state_passed_is_list():
     with pytest.raises(InvalidInput):
          Bell([150],12)

@pytest.mark.errors
def test_that_error_raised_when_current_state_passed_is_string():
     with pytest.raises(InvalidInput):
          Bell("75",12)

@pytest.mark.errors
def test_that_error_raised_when_max_lifespan_passed_is_out_of_range():
     with pytest.raises(InvalidInput):
          Bell(75,-12)

@pytest.mark.errors
def test_that_error_raised_when_max_lifespan_passed_is_list():
     with pytest.raises(InvalidInput):
          Bell(75,-12)

@pytest.mark.errors
def test_that_error_raised_when_max_lifespan_passed_is_string():
     with pytest.raises(InvalidInput):
          Bell(75,-12)

@pytest.mark.errors
def test_that_error_raised_when_bike_made_without_required_components():
     with pytest.raises(TypeError):    
          new_bell = Bell(88,8)
          new_brakes = Brakes(85,12.5)
          new_chain = Chain(92,5)
          new_tyres = Tyres(98,20)
          new_bike = Bike(new_bell, new_brakes, new_chain, new_tyres)
          # could also test that each component is of the correct class
          # ie pedals given to Bike are from the pedals class

# def test_that_racing_bike_sub_class_increases_wear_on_tyres_and_chain_by_5pc():
#      new_bell = Bell(88,8)
#      new_brakes = Brakes(85,12.5)
#      new_chain = Chain(92,5)
#      new_tyres = Tyres(98,20)
#      new_pedals = Pedals(44,10)
#      new_racing_bike = RacingBike(new_bell, new_brakes, new_chain, new_tyres, new_pedals)
#      new_racing_bike.ride()
     # assert new_racing_bike.tyres.current_state == 92.75
     # assert new_racing_bike.chain.current_state == 71