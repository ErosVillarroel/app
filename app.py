import json
from flask import Flask, jsonify, request
import requests
from pymongo import MongoClient
import certifi
import uuid
import os

#from dotenv import load_dotenv, find_dotenv
import datetime
import traceback