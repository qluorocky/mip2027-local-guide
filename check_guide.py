"""Run with python3 check_guide.py. Checks the shared map/list/table data."""
from pathlib import Path
from html.parser import HTMLParser
import re,json,subprocess,tempfile
s=Path('dist/index.html').read_text()
p=json.loads(re.search(r'<script id="mip-places-data"[^>]*>(.*?)</script>',s,re.S).group(1))
class Elements(HTMLParser):
    def __init__(self): super().__init__();self.cards=[];self.links=[];self.ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.append(a['id'])
        if 'place-card' in a.get('class','').split():self.cards.append(a['data-id'])
        if a.get('data-locate'):self.links.append(a['data-locate'])
e=Elements();e.feed(s)
ids=[x['id'] for x in p]
assert len(p)==42 and len(set(ids))==42
assert e.cards==ids and set(e.links)==set(ids)
assert len(e.ids)==len(set(e.ids)), 'Duplicate HTML IDs'
venues=[x for x in p if x['category']=='venue']
assert len(venues)==2 and 'Tippie' in venues[0]['name'] and 'Graduate' in venues[1]['name']
assert not re.search(r'\bIMU\b|Iowa Memorial Union',s,re.I)
assert len([x for x in p if x['category']=='event'])==6
assert len([x for x in p if x['category']=='dining'])==18
for x in p:
    assert 41.64<x['lat']<41.69 and -91.57<x['lng']<-91.51
    assert x['url'].startswith(('https://','http://'))
    if x['category']=='event':assert x.get('schedule') and x.get('eventStatus')
added=[x for x in p if int(x['id'])>=33]
assert len(added)==10
assert len([x for x in added if x['category']=='coffee'])==4
for x in added:
    assert x['googleRating']>3.5 and x['googleReviewCount']>0
    assert x['ratingChecked']=='2026-11-12'
    assert x['ratingSource'].startswith('https://www.google.com/maps/place/')
    point=re.search(r'!3d(-?[\d.]+)!4d(-?[\d.]+)',x['ratingSource'])
    assert (x['lat'],x['lng'])==(float(point[1]),float(point[2]))
assert '<option>Mexican</option>' in s
assert 'area-filter' in e.ids and 'food-filter' in e.ids
for i,script in enumerate(re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>',s,re.S)):
    if script.strip().startswith('[{'):continue
    with tempfile.NamedTemporaryFile(suffix='.js',mode='w') as f:
        f.write(script);f.flush();subprocess.run(['node','--check',f.name],check=True,capture_output=True)
print('PASS: 42 map/list entries; 10 new Google ratings >3.5 with source coordinates; 2 venues; 18 restaurants; 10 cafes; 6 events; links, IDs and JavaScript syntax.')
