#!/usr/bin/env python
#******************************************************************************
# (C) 2014, Stefan Korner, Austria                                            *
#                                                                             *
# The Space Python Library is free software; you can redistribute it and/or   *
# modify it under the terms of the GNU Lesser General Public License as       *
# published by the Free Software Foundation; either version 2.1 of the        *
# License, or (at your option) any later version.                             *
#                                                                             *
# The Space Python Library is distributed in the hope that it will be useful, *
# but WITHOUT ANY WARRANTY; without even the implied warranty of              *
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser     *
# General Public License for more details.                                    *
#******************************************************************************
# Unit Tests                                                                  *
#******************************************************************************
import os, sys
from UTIL.SYS import Error, LOG, LOG_INFO, LOG_WARNING, LOG_ERROR
import UTIL.SYS, UTIL.TCP

#############
# functions #
#############
# -----------------------------------------------------------------------------
def initConfiguration():
  """initialise the system configuration"""
  UTIL.SYS.s_configuration.setDefaults([
    ["HOST", "192.168.1.100"],
    ["SERVER_PORT", "1234"]])
# -----------------------------------------------------------------------------
def createClient():
  """create the TCP client"""
  client = UTIL.TCP.Client()
  dataSocket = client.connectToServer(
    UTIL.SYS.s_configuration.HOST,
    int(UTIL.SYS.s_configuration.SERVER_PORT))
  if not dataSocket:
    sys.exit(-1)
  return dataSocket

########
# main #
########
if __name__ == "__main__":
  # initialise the system configuration
  initConfiguration()
  # create the TCP client
  LOG("Open the TCP client")
  dataSocket = createClient()
  # force termination of the server
  LOG("force server termination...")
  dataSocket.send("quit\n")
  dataSocket.close()
