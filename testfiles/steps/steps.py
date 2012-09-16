from radish import *

@step(r'I have the number (\d+)')
def have_the_number(step, number):
  world.number = int(number)

@step(r'I compute its factorial')
def compute_its_factorial(step):
  world.number = factorial(world.number)

@step(r'I see the number (\d+)')
def check_number(step, expected):
  expected = int(expected)
  assert world.number == expected, "Got %d" % world.number

def factorial(number):
  return -1
