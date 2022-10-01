from flask import Flask, render_template, request, session, redirect
import json, lastfm_base, get_api


app = Flask(__name__)
app.secret_key = "BBS my diamonds, I don't need no light to shine"


@app.route('/')
def hello_world():
    return redirect('/create')


obj = lastfm_base.LastFM_Data()
toptracks = obj.lastfm_get_data()
obj.print_data()
