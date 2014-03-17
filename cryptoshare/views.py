from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from cryptoshare.forms import RawMessageForm
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
    key = request.POST.get('key', None)
    id = base62_converter.saturate(base_62)
    doc = Document.objects.get(id=id)

    if key is not None:
        plaintext = doc.decrypt(key)
    else:
        plaintext = None

    if request.is_ajax():
        return HttpResponse(plaintext)
    else:

        return render(request, 'encrypted.html',
                  {
                      'document': doc,
                      'plaintext': plaintext,
                      'url' : base_62,
                  })
