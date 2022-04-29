#!/usr/bin/env python3

import sys
import torch
from unixcoder import UniXcoder

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UniXcoder("microsoft/unixcoder-base")
model.to(device)

init_context = "<mask0>"

def probe(context):
    tokens_ids = model.tokenize([context],max_length=512,mode="<encoder-decoder>")
    source_ids = torch.tensor(tokens_ids).to(device)
    prediction_ids = model.generate(source_ids, decoder_only=False, beam_size=3, max_length=128)
    predictions = model.decode(prediction_ids)
    output = [x.replace("<mask0>","").strip() for x in predictions[0]][0]
    return output

if __name__ == "__main__":
    if len(sys.argv) == 1:
        #context = init_context
        #for i in range(10):
        #    print(context)
        #    new_context = probe(context)
        #    print(new_context)
        #    context = new_context + "\n<mask0>"
        #print(context)
        print(probe(init_context))
    else:
        with open(sys.argv[1], 'r') as f:
            masked_code = f.read()
            print(probe(masked_code))
