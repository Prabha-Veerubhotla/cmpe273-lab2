"""The Python implementation of the GRPC Calculator.Calculator client."""

from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = calculator_pb2_grpc.CalculatorStub(channel)
  response = stub.AddTwoNumbers(calculator_pb2.AddRequest(a=1, b=-5))
  print("Sum of the given two numbers is: %s" % response.sum)
  

if __name__ == '__main__':
    run()
