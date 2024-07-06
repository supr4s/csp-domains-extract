Extract the domains present in a CSP policy

## Installation & usage

```
$ git clone https://github.com/supr4s/csp-domains-extract.git && cd csp-domains-extract && chmod +x csp-domains-extract.py
```

Scan a single URL

```
$ python csp-domains-extract.py -u https://paypal.com -o paypal-csp-results
[...]
api.paypal-retaillocator.com
assets-cdn.s-xoom.com
force.com
nexus.ensighten.com
nominatim.openstreetmap.org
paypal-corp.com
paypal-mktg.com
paypal.com
paypal.us-4.evergage.com
paypalobjects.com
pypd.paypal-mktg.com
[...]
```

Scan multiple URLs and store the result in a file

```
$ python csp-domains-extract.py -ul paypal-domains -o paypal-csp-results
Results saved to paypal-csp
```

```
$ cat paypal-csp
[...]
api.paypal-retaillocator.com
assets-cdn.s-xoom.com
force.com
nexus.ensighten.com
nominatim.openstreetmap.org
paypal-corp.com
paypal-mktg.com
paypal.com
paypal.us-4.evergage.com
paypalobjects.com
pypd.paypal-mktg.com
[...]
```
