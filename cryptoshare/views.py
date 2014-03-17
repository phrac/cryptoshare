from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

from cryptoshare.forms import RawMessageForm, DecodeForm
from cryptoshare.models import Document

import base62_converter

import hashlib
from Crypto.Cipher import AES
import os, binascii, base64

def index(request):
    if request.method == 'POST':
        form = RawMessageForm(request.POST)
        if form.is_valid():
            msg = form.cleaned_data['message']
            key = form.cleaned_data['key']
            doc = Document()
            doc.ciphertext = doc.encrypt(msg, key)
            doc.save()

            url = base62_converter.dehydrate(doc.id)

            return HttpResponseRedirect(reverse('cryptoshare.views.viewmsg',
                                                args=[url]))
    else:
        form = RawMessageForm(None)

    return render(request, 'index.html', {'form': form})


def viewmsg(request, base_62):
    try:
        id = base62_converter.saturate(base_62)
    except:
        return Http404
    doc = get_object_or_404(Document, pk=id)
    plaintext = None
    
    if request.method == 'POST':
        form = DecodeForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            plaintext = doc.decrypt(key)
    else:
        form = DecodeForm(None)

    if request.is_ajax():
        return HttpResponse(plaintext)
    else:

        return render(request, 'encrypted.html',
                  {
                      'document': doc,
                      'plaintext': plaintext,
                      'url' : base_62,
                      'form': form,
                  })
