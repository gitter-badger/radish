# -*- coding: utf-8 -*-

from radish import step, world
from time import sleep


@step(r'I have the number ([+0-9-]+)', metric_indicators=['a', 'c'])
def have_the_number(step, number):
    if int(number) < 0:
        step.ValidationError("The number cannot be nagative")
        return

    world.number = 0
    if not step.is_dry_run():
        world.number = int(number)
        sleep(1)


@step(r'I compute its factorial', metric_indicators=['b', 'c'])
def compute_its_factorial(step):
    if not step.is_dry_run():
        world.number = factorial(world.number)
        sleep(1)


@step(r'I see the number (\d+)', metric_indicators=['a', 'b', 'c'])
def check_number(step, expected):
    if not step.is_dry_run():
        expected = int(expected)
        sleep(1)
        assert world.number == expected, "Got %d" % world.number


@step(r'(dfg)+')
def dfg(step, dfg):
    if not step.is_dry_run():
        sleep(1)


@step(r'I fail after (\d+) times')
def fail_after_times(step, times):
    times = int(times)
    if world.fail_after_times_count >= times:
        assert False, "Sorry, but it's the %d time" % times
    world.fail_after_times_count += 1

@step(u'I have a address table')
def I_have_a_address_card(step, Table):
    rows = Table.create_set()
    assert len(rows) == 2
    assert rows[0].Name     == "Hans"
    assert rows[0].Lastname == "Dampf"
    assert rows[0].Street   == "In allen Gassen"
    assert rows[0].ZIP      == "4242"
    assert rows[0].City     == "Buxdehude"
    assert rows[1].Name     == "Donald"
    assert rows[1].Lastname == "Duck"
    assert rows[1].Street   == "I don't know"
    assert rows[1].ZIP      == "1234"
    assert rows[1].City     == "Entenhausen"

@step(u'I have a address card')
def I_have_a_address_card(step, Table):
    """ Use a table as a single instance object """
    prop = Table.create_instance()
    assert prop.Name == "Hans"
    assert prop.Lastname == "Dampf"
    assert prop.Street == "In allen Gassen"
    assert prop.ZIP == "4242"
    assert prop.City == "Buxdehude"

def factorial(number):
    from math import factorial
    return factorial(number)


@step(r'I add this to (\d+)')
def add_this_to(step, number):
    world.result = int(number) + world.number


@step(r'I see the sum (\d+)')
def see_the_sum(step, result):
    assert int(result) == world.result, "Result is %d. Expected is %s" % (world.result, result)


@step(r'I have the numbers (\d+) and (\d+)')
def have_the_numbers(step, number1, number2):
    world.number1 = int(number1)
    world.number2 = int(number2)


@step(r'I sum these numbers')
def sum_these_numbers(step):
    sleep(1)
    world.result = world.number1 + world.number2
