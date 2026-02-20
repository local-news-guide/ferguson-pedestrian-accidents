"""Generate city pages with consistent HTML structure."""
import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{city} Pedestrian Accident Lawyer | Ferguson &amp; Ferguson</title>
  <meta name="description" content="Pedestrian accident attorney in {city}, Alabama. {meta_desc} Free consultation: (256) 555-5555.">
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

<div class="ff-topbar"><div class="ff-container ff-topbar__inner"><span>Serving Cullman County &amp; All of North Alabama</span><a href="tel:+12565555555">(256) 555-5555</a></div></div>

<header class="ff-header"><div class="ff-container ff-header__inner"><a href="../index.html" class="ff-logo">Ferguson <span>&amp;</span> Ferguson</a><nav class="ff-nav"><a href="../index.html">Home</a><a href="../index.html#cities">Service Areas</a><a href="#about">About</a><a href="#contact">Contact</a><a href="tel:+12565555555" class="ff-nav__phone">(256) 555-5555</a></nav><button class="ff-nav-toggle" aria-label="Toggle navigation"><span></span><span></span><span></span></button></div></header>

<section class="ff-hero">
  <div class="ff-container">
    <div class="ff-hero__location">&#9906; {city}, Alabama</div>
    <h1>{city} <span>Pedestrian Accident Lawyer</span></h1>
    <p class="ff-lead">{hero_lead}</p>
    <a href="#contact" class="ff-btn ff-btn--gold ff-btn--lg">Free Consultation</a>
    <a href="tel:+12565555555" class="ff-btn ff-btn--outline ff-btn--lg">Call (256) 555-5555</a>
  </div>
</section>

<!-- Table of Contents -->
<div class="ff-toc">
  <div class="ff-toc__title">On This Page</div>
  <ul class="ff-toc__list">
    <li><a href="#accidents">Pedestrian Accidents in {city}</a></li>
    <li><a href="#causes">Common Causes</a></li>
    <li><a href="#laws">Alabama Pedestrian Law</a></li>
    <li><a href="#steps">What to Do After an Accident</a></li>
    <li><a href="#about">Why Choose Ferguson &amp; Ferguson</a></li>
    <li><a href="#contact">Contact Us</a></li>
  </ul>
</div>

<section id="accidents" class="ff-section"><div class="ff-container"><div class="ff-two-col"><div><img src="{image}" alt="{city} Alabama" class="ff-two-col__img"></div><div>
  <span class="ff-eyebrow">{city} Pedestrian Accidents</span>
  <h2 class="ff-mb-3">{intro_h2}</h2>
  <p class="ff-mb-3">{intro_p1}</p>
  <p class="ff-mb-3">{intro_p2}</p>
  <p>{intro_p3}</p>
</div></div></div></section>

<section id="causes" class="ff-section ff-section--gray"><div class="ff-container"><div class="ff-text-center ff-mb-5"><span class="ff-eyebrow">Common Causes</span><h2>Why Pedestrian Accidents Happen in {city}</h2></div>
  <ul class="ff-icon-list ff-icon-list--2col">
    <li><div class="ff-icon-list__icon">1</div><div class="ff-icon-list__text"><h4>{c1_title}</h4><p>{c1_text}</p></div></li>
    <li><div class="ff-icon-list__icon">2</div><div class="ff-icon-list__text"><h4>{c2_title}</h4><p>{c2_text}</p></div></li>
    <li><div class="ff-icon-list__icon">3</div><div class="ff-icon-list__text"><h4>{c3_title}</h4><p>{c3_text}</p></div></li>
    <li><div class="ff-icon-list__icon">4</div><div class="ff-icon-list__text"><h4>{c4_title}</h4><p>{c4_text}</p></div></li>
    <li><div class="ff-icon-list__icon">5</div><div class="ff-icon-list__text"><h4>{c5_title}</h4><p>{c5_text}</p></div></li>
    <li><div class="ff-icon-list__icon">6</div><div class="ff-icon-list__text"><h4>{c6_title}</h4><p>{c6_text}</p></div></li>
  </ul>
</div></section>

<section id="laws" class="ff-section"><div class="ff-container--narrow">
  <span class="ff-eyebrow">Alabama Pedestrian Law</span>
  <h2 class="ff-mb-4">Know Your Rights as a Pedestrian in Alabama</h2>
  <div class="ff-law-box"><h3>&#9878; Key Alabama Pedestrian Laws</h3><ul>
    <li>Drivers must yield to pedestrians in marked crosswalks (Ala. Code &sect; 32-5A-210)</li>
    <li>Pedestrians have the right-of-way at signalized intersections when the walk signal is active</li>
    <li>Alabama follows <strong>contributory negligence</strong> &mdash; if you are found even 1% at fault, you could lose your entire claim</li>
    <li>Drivers must exercise due care to avoid striking pedestrians on any roadway (Ala. Code &sect; 32-5A-214)</li>
    <li>Hit-and-run drivers face criminal charges, and you may still recover through uninsured motorist coverage</li>
    <li>The statute of limitations for personal injury in Alabama is <strong>2 years</strong> from the date of the accident</li>
  </ul></div>
  <div class="ff-callout"><p><strong>{callout_bold}</strong> {callout_text}</p></div>
</div></section>

<section id="steps" class="ff-section ff-section--gray"><div class="ff-container--narrow">
  <span class="ff-eyebrow">After an Accident</span>
  <h2 class="ff-mb-4">What to Do After a Pedestrian Accident in {city}</h2>
  <ol class="ff-steps">
    <li><div><h4>Call 911 Immediately</h4><p>{step1}</p></div></li>
    <li><div><h4>Seek Medical Attention</h4><p>{step2}</p></div></li>
    <li><div><h4>Document Everything</h4><p>{step3}</p></div></li>
    <li><div><h4>Do Not Give Recorded Statements</h4><p>The driver's insurance company will call quickly. They want statements to twist against you under Alabama's contributory negligence rule. Politely decline and refer them to your attorney.</p></div></li>
    <li><div><h4>Call Ferguson &amp; Ferguson</h4><p>The sooner we are involved, the better we can preserve evidence and protect your claim. Free consultation &mdash; call (256) 555-5555.</p></div></li>
  </ol>
</div></section>

<section id="about" class="ff-section ff-section--navy"><div class="ff-container"><div class="ff-text-center ff-mb-5"><span class="ff-eyebrow">Why {city} Trusts Us</span><h2>Ferguson &amp; Ferguson Knows {city}</h2></div>
  <ul class="ff-icon-list ff-icon-list--2col">
    <li><div class="ff-icon-list__icon">&#9878;</div><div class="ff-icon-list__text"><h4>{why1_title}</h4><p>{why1_text}</p></div></li>
    <li><div class="ff-icon-list__icon">&#9733;</div><div class="ff-icon-list__text"><h4>Maximum Compensation Strategy</h4><p>We don't settle for quick lowball offers. We calculate the full value &mdash; medical costs, lost income, pain and suffering, and future care needs.</p></div></li>
    <li><div class="ff-icon-list__icon">&#128176;</div><div class="ff-icon-list__text"><h4>No Fee Unless We Win</h4><p>Zero upfront cost. We only get paid when you get paid.</p></div></li>
    <li><div class="ff-icon-list__icon">&#9742;</div><div class="ff-icon-list__text"><h4>Available 24/7</h4><p>Accidents don't wait for business hours. Neither do we. Call anytime.</p></div></li>
  </ul>
</div></section>

<section id="contact" class="ff-cta"><div class="ff-container"><h2>Injured While Walking in {city}?</h2><p>Don't let the insurance company undervalue your claim. Contact Ferguson &amp; Ferguson today for a free consultation.</p><a href="tel:+12565555555" class="ff-btn ff-btn--gold ff-btn--lg">Call (256) 555-5555</a><a href="mailto:info@fergusonandferguson.com" class="ff-btn ff-btn--white ff-btn--lg">Email Us</a></div></section>

<footer class="ff-footer"><div class="ff-container"><div class="ff-footer__grid">
  <div><div class="ff-footer__logo">Ferguson <span>&amp;</span> Ferguson</div><p>Personal injury attorneys serving Cullman County and all of North Alabama.</p><p class="ff-footer__disclaimer">The information on this website is for general information purposes only. Nothing on this site should be taken as legal advice for any individual case or situation.</p></div>
  <div><h4>Service Areas</h4><ul><li><a href="cullman.html">Cullman</a></li><li><a href="hanceville.html">Hanceville</a></li><li><a href="good-hope.html">Good Hope</a></li><li><a href="baileyton.html">Baileyton</a></li><li><a href="berlin.html">Berlin</a></li><li><a href="colony.html">Colony</a></li></ul></div>
  <div><h4>More Areas</h4><ul><li><a href="dodge-city.html">Dodge City</a></li><li><a href="fairview.html">Fairview</a></li><li><a href="garden-city.html">Garden City</a></li><li><a href="holly-pond.html">Holly Pond</a></li><li><a href="south-vinemont.html">South Vinemont</a></li><li><a href="west-point.html">West Point</a></li></ul></div>
  <div><h4>Contact</h4><ul><li><a href="tel:+12565555555">(256) 555-5555</a></li><li><a href="mailto:info@fergusonandferguson.com">Email Us</a></li><li>Cullman, Alabama</li></ul></div>
</div><div class="ff-footer__bottom"><span>&copy; 2026 Ferguson &amp; Ferguson. All rights reserved.</span><span>Pedestrian Accident Lawyers &bull; {city}, Alabama</span></div></div></footer>

</body>
</html>"""

cities = [
    dict(file='berlin', city='Berlin', meta_desc='Rural road pedestrian injuries and agricultural traffic accidents.',
         image='https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=640&h=400&fit=crop',
         hero_lead='Berlin\'s narrow county roads have no shoulders, no sidewalks, and no streetlights. When pedestrians have nowhere to go and negligent drivers aren\'t paying attention, devastating accidents happen.',
         intro_h2='Rural Roads Where Pedestrians Have No Safe Space',
         intro_p1='Berlin is a small agricultural community in Cullman County where narrow county roads serve as the only path for both vehicles and pedestrians. There are no sidewalks, no paved shoulders, and no street lights on most roads. When residents walk to check their mail, visit a neighbor, or get exercise, they share the road with cars, trucks, and farm equipment.',
         intro_p2='The lack of any pedestrian infrastructure means that when a driver is distracted, speeding, or impaired, there is literally nowhere for a pedestrian to go. Ditches on one side, fast-moving traffic on the other &mdash; Berlin\'s roads force an impossible choice on people who simply need to walk.',
         intro_p3='Ferguson &amp; Ferguson represents pedestrians injured on Cullman County\'s rural roads. We understand that the absence of sidewalks does not make walking negligent &mdash; and we fight to make sure insurance companies can\'t use rural infrastructure failures against you.',
         c1_title='Narrow Roads With No Shoulders', c1_text='Berlin\'s county roads have pavement that ends abruptly at ditches or grass. Pedestrians have inches of space between themselves and passing vehicles.',
         c2_title='Zero Sidewalk Infrastructure', c2_text='There are no sidewalks anywhere in Berlin. Residents walking for exercise, to visit neighbors, or to check mail must use the roadway itself.',
         c3_title='Farm Equipment Blocking Visibility', c3_text='Tractors, combines, and other agricultural equipment sharing narrow roads force pedestrians into ditches and block drivers\' views of people on foot.',
         c4_title='No Street Lighting', c4_text='Most Berlin roads are completely unlit after sunset. Pedestrians become invisible to drivers, especially on overcast evenings.',
         c5_title='Excessive Speed on County Roads', c5_text='Drivers treat rural county roads like highways, reaching speeds far above what is safe for roads shared with pedestrians and farm equipment.',
         c6_title='No Crossings or Warning Signs', c6_text='Berlin has no marked crosswalks, no pedestrian crossing signs, and no traffic signals of any kind. Drivers receive zero warning that pedestrians may be ahead.',
         callout_bold='No sidewalk doesn\'t mean no rights.', callout_text='Insurance companies will blame you for walking on a road without a sidewalk. But when there is no alternative infrastructure, Alabama law still requires drivers to exercise due care. Ferguson &amp; Ferguson knows how to fight this argument.',
         step1='Call 911. Rural response times in Berlin may be longer. The Cullman County Sheriff and county EMS will respond. An official police report is critical evidence.',
         step2='Get checked at Cullman Regional Medical Center even if injuries seem minor. Rural road impacts at speed cause serious internal injuries that may not appear for hours.',
         step3='Photograph the scene, road conditions, lack of shoulders and lighting, your injuries, and the vehicle. Document the infrastructure failures that contributed to the accident.',
         why1_title='Rural Road Accident Experience', why1_text='We know Berlin\'s county roads, the agricultural traffic patterns, and how rural infrastructure failures contribute to pedestrian accidents.'),

    dict(file='colony', city='Colony', meta_desc='County road pedestrian injuries and small-town walking accidents.',
         image='https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=640&h=400&fit=crop',
         hero_lead='Colony is a quiet community of about 350 people where residents walk to visit neighbors, walk their dogs, and gather for church. But shared roadways with fast-moving traffic make every walk a risk.',
         intro_h2='A Quiet Community Where Shared Roads Create Danger',
         intro_p1='Colony sits along County Road 222 in Cullman County &mdash; a tight-knit community of roughly 350 people where walking is simply part of daily life. Residents walk between neighbors\' homes, jog along the road for exercise, and walk their dogs on the same roadways used by vehicles traveling far too fast.',
         intro_p2='With no sidewalks, no crosswalks, and no traffic controls, Colony\'s roads offer zero protection for pedestrians. Community events and church gatherings periodically create clusters of people on foot, but drivers passing through rarely slow down.',
         intro_p3='Ferguson &amp; Ferguson represents pedestrians struck on Colony\'s county roads. We understand that small-town walking culture is not negligence &mdash; and we hold drivers accountable when their carelessness injures people in this community.',
         c1_title='Shared Roadways With No Sidewalks', c1_text='Colony has zero dedicated pedestrian infrastructure. Walkers, joggers, and dog walkers share the road surface with vehicles, separated by nothing.',
         c2_title='Speeding on County Roads', c2_text='Drivers treat County Road 222 like open highway, reaching speeds that give them no time to react to pedestrians around curves or over hills.',
         c3_title='Dog Walkers and Joggers at Risk', c3_text='Residents who walk dogs or jog along Colony\'s roads are forced onto narrow shoulders or the road itself, especially where ditches line the roadside.',
         c4_title='Blind Curves and Hills', c4_text='Colony\'s winding county roads feature curves and hills that hide pedestrians from approaching drivers until it is too late to stop.',
         c5_title='Church and Community Event Traffic', c5_text='When Colony\'s churches and community gatherings let out, groups of pedestrians walk along roads simultaneously &mdash; creating unexpected foot traffic.',
         c6_title='No Lighting After Dark', c6_text='Colony\'s roads have no street lighting. Evening walkers and anyone returning from a neighbor\'s home after sunset is essentially invisible to drivers.',
         callout_bold='Small-town walking is not carelessness.', callout_text='Insurance companies will argue you shouldn\'t have been walking on a road without sidewalks. Ferguson &amp; Ferguson fights back by proving the driver\'s negligence was the sole cause of your injuries.',
         step1='Call 911. The Cullman County Sheriff and county EMS will respond. An official police report documenting the scene is essential evidence.',
         step2='Even if you feel okay, go to Cullman Regional Medical Center. Pedestrian impacts cause internal injuries that may not show symptoms for hours.',
         step3='Photograph the road, lack of shoulders, blind curves, lighting conditions, your injuries, and the vehicle. Get witness contact info from neighbors who saw the accident.',
         why1_title='Rural Community Expertise', why1_text='We understand Colony\'s roads, its walking culture, and how to prove that infrastructure failures &mdash; not pedestrian behavior &mdash; caused the accident.'),

    dict(file='dodge-city', city='Dodge City', meta_desc='Pedestrian injuries in growing neighborhoods and construction zones.',
         image='https://images.unsplash.com/photo-1494783367193-149034c05e8f?w=640&h=400&fit=crop',
         hero_lead='Dodge City is growing fast, but new subdivisions have no sidewalks, no streetlights, and construction traffic shares roads with families on foot. When development outpaces safety, pedestrians get hurt.',
         intro_h2='New Development, Missing Safety Infrastructure',
         intro_p1='Dodge City is one of Cullman County\'s emerging growth areas, with new homes and subdivisions drawing families to the community. But residential development has far outpaced pedestrian safety planning. New neighborhoods connect to town via roads with no sidewalks, no streetlights, and no safe crossings.',
         intro_p2='Construction vehicles sharing residential roads with pedestrians add another layer of danger. Dump trucks, concrete mixers, and heavy equipment operate alongside families walking to neighbors\' homes and children playing near the road.',
         intro_p3='Ferguson &amp; Ferguson represents pedestrians injured in Dodge City\'s growing but underserved neighborhoods. We hold negligent drivers and construction operators accountable when their carelessness injures people on foot.',
         c1_title='New Subdivisions Without Sidewalks', c1_text='Dodge City\'s newest neighborhoods were built without pedestrian infrastructure. Families walk along road edges to reach town, bus stops, or neighbors\' homes.',
         c2_title='Construction Vehicle Traffic', c2_text='Heavy construction vehicles serving active building sites share narrow residential roads with pedestrians, creating dangerous blind spots.',
         c3_title='Children Walking Without Safe Paths', c3_text='Without sidewalks, children in new neighborhoods walk along roads to reach bus stops, friends\' houses, and community areas.',
         c4_title='No Streetlights in New Areas', c4_text='Many newly developed sections lack street lighting. Evening walkers and children playing near roads after school become invisible to drivers.',
         c5_title='Speeding in Residential Zones', c5_text='Drivers cutting through residential areas often exceed safe speeds, especially on straight stretches between subdivisions.',
         c6_title='Disconnected Neighborhoods', c6_text='New subdivisions connect only by roads without shoulders or pedestrian facilities. Walking between neighborhoods means sharing the road with traffic.',
         callout_bold='Developers and drivers share responsibility.', callout_text='When neighborhoods are built without sidewalks and a driver strikes a pedestrian, both the infrastructure failure and the driver\'s negligence may be at play. Ferguson &amp; Ferguson investigates all angles.',
         step1='Call 911. Cullman County Sheriff and EMS will respond. Ensure a police report is filed documenting road conditions and lack of pedestrian infrastructure.',
         step2='Go to Cullman Regional Medical Center even if injuries seem minor. Pedestrian impacts &mdash; even at lower residential speeds &mdash; cause serious internal injuries.',
         step3='Photograph the road, lack of sidewalks and lighting, construction activity, your injuries, and the vehicle. Note any construction company names on vehicles or signs.',
         why1_title='Development Area Expertise', why1_text='We understand how growth-area infrastructure failures contribute to pedestrian accidents and know how to build cases against both drivers and negligent developers.'),

    dict(file='fairview', city='Fairview', meta_desc='US-278 truck traffic pedestrian injuries and highway crossing accidents.',
         image='https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=640&h=400&fit=crop',
         hero_lead='Located along US-278, Fairview sees heavy truck and commuter traffic roaring past homes and businesses. Pedestrians crossing the highway or walking along its shoulders face life-threatening danger every day.',
         intro_h2='Living Alongside a Dangerous Highway Corridor',
         intro_p1='Fairview straddles US-278, a busy east-west highway that carries heavy truck traffic, commercial vehicles, and daily commuters through this 800-person community. Homes, businesses, and churches line both sides of the highway, forcing residents to cross or walk alongside fast-moving traffic for basic daily tasks.',
         intro_p2='The combination of 18-wheelers, commercial vehicles, and commuters traveling at highway speed creates a particularly dangerous environment. Large trucks have massive blind spots and require far greater stopping distances. When a truck driver fails to see a pedestrian crossing US-278, the results are catastrophic.',
         intro_p3='Ferguson &amp; Ferguson represents pedestrians injured along the US-278 corridor through Fairview. We know how to investigate truck and commercial vehicle accidents and hold negligent drivers and trucking companies accountable.',
         c1_title='Heavy Truck Traffic', c1_text='US-278 carries a constant stream of 18-wheelers and commercial vehicles. Their massive blind spots and long stopping distances make them especially deadly to pedestrians.',
         c2_title='Dangerous Highway Crossings', c2_text='Fairview residents must cross US-278 to reach businesses, churches, and neighbors on the opposite side. Without crosswalks or signals, every crossing is a gamble.',
         c3_title='Excessive Speed', c3_text='Drivers and truckers maintaining highway speed through Fairview can\'t stop in time when pedestrians appear at driveways, intersections, or road shoulders.',
         c4_title='Commercial Vehicle Blind Spots', c4_text='Large trucks have blind spots on all four sides. Pedestrians visible to a car driver may be completely invisible to a trucker making a right turn.',
         c5_title='Limited Visibility at Curves', c5_text='Sections of US-278 through Fairview feature curves that hide pedestrians from approaching vehicles until the last moment.',
         c6_title='No Pedestrian Signals', c6_text='Fairview has no pedestrian crossing signals along the US-278 corridor. Residents must judge gaps in highway traffic themselves when crossing.',
         callout_bold='Truck accidents require specialized investigation.', callout_text='Commercial vehicles carry electronic logs, dashcam footage, and maintenance records that can prove negligence. Ferguson &amp; Ferguson knows how to obtain this evidence before trucking companies destroy it.',
         step1='Call 911 immediately. US-278 accidents often involve heavy vehicles and severe injuries. Ensure law enforcement documents any commercial vehicle information.',
         step2='Go to Cullman Regional Medical Center immediately. Truck-pedestrian impacts cause catastrophic injuries requiring urgent evaluation.',
         step3='Photograph everything: the truck, company markings, license plates, your injuries, road conditions, and the lack of crosswalks or pedestrian signals.',
         why1_title='Truck Accident Expertise', why1_text='We know how to investigate commercial vehicle accidents, obtain electronic logs and dashcam footage, and hold trucking companies accountable.'),

    dict(file='garden-city', city='Garden City', meta_desc='School zone pedestrian injuries and residential area accidents.',
         image='https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=640&h=400&fit=crop',
         hero_lead='Garden City is growing, but pedestrian safety hasn\'t kept pace. From school zones near Garden City Elementary to residential roads without sidewalks, people on foot face real danger from careless drivers.',
         intro_h2='A Growing Town Where Pedestrian Safety Lags Behind',
         intro_p1='Garden City is experiencing steady growth that transforms a rural community into a suburban one. With a population around 800 and climbing, more families, more vehicles, and more foot traffic share roads designed for a fraction of today\'s use.',
         intro_p2='Garden City Elementary School is a particular concern. Twice daily, children and parents navigate roads without adequate crosswalks, crossing guards, or reduced-speed enforcement. Drivers who fail to slow in school zones put the community\'s most vulnerable members at risk.',
         intro_p3='Ferguson &amp; Ferguson represents pedestrians injured in Garden City &mdash; from schoolchildren struck in crosswalks to residents hit while walking along roads with no sidewalks.',
         c1_title='School Zone Violations', c1_text='Drivers who speed through Garden City Elementary\'s school zone or fail to yield to crossing pedestrians endanger children and parents every school day.',
         c2_title='Roads Without Sidewalks', c2_text='Most Garden City streets lack sidewalks. Residents walking to neighbors, the store, or the bus stop must share the road with vehicles.',
         c3_title='Increasing Traffic Volume', c3_text='Population growth has dramatically increased traffic on roads not designed for current volumes, creating more opportunities for pedestrian-vehicle conflicts.',
         c4_title='Speed in Residential Areas', c4_text='Drivers cutting through residential streets often exceed safe speeds, especially on straight sections where they fail to anticipate pedestrians.',
         c5_title='Children Walking Without Protection', c5_text='Without sidewalks or safe walking paths, children walk along road edges to reach school, bus stops, and friends\' homes &mdash; a daily risk no family should face.',
         c6_title='Poor Road Design', c6_text='Roads built for rural traffic now serve suburban density. Narrow lanes, missing shoulders, and inadequate sight lines create pedestrian hazards.',
         callout_bold='Children deserve better protection.', callout_text='When a driver strikes a child in a school zone or on a residential road, the consequences are devastating. Ferguson &amp; Ferguson holds negligent drivers fully accountable.',
         step1='Call 911. Garden City Police or Cullman County Sheriff will respond. If a child is involved, request EMS immediately regardless of apparent injury severity.',
         step2='Take your child or yourself to Cullman Regional Medical Center. Children are especially vulnerable to head injuries and internal trauma from pedestrian impacts.',
         step3='Photograph the scene, the vehicle, injuries, road conditions, school zone signage, and any lack of crosswalks. Get contact information from witnesses.',
         why1_title='School Zone Accident Experience', why1_text='We understand the heightened duty of care drivers owe in school zones and residential areas, and we build cases that hold them to that standard.'),

    dict(file='holly-pond', city='Holly Pond', meta_desc='Highway 31 pedestrian injuries and school zone accidents.',
         image='https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?w=640&h=400&fit=crop',
         hero_lead='Holly Pond is a tight-knit community of 800 people bisected by Highway 31. When high-speed traffic meets a town where walking is a way of life, pedestrians face dangers that demand experienced legal representation.',
         intro_h2='A Walking Town Bisected by a Federal Highway',
         intro_p1='Holly Pond sits directly on Highway 31, one of Alabama\'s busiest north-south corridors. The town\'s commercial center, schools, and churches line the highway, meaning residents must interact with high-speed through-traffic for nearly every daily errand.',
         intro_p2='Highway 31 was not designed for pedestrians. Many drivers maintain highway velocity through town, giving them little time to react to pedestrians at driveways, intersections, or walking along narrow shoulders. Holly Pond High School adds another layer of concern with students creating periodic surges in foot traffic.',
         intro_p3='Ferguson &amp; Ferguson represents Holly Pond pedestrians injured by negligent drivers on Highway 31 and surrounding roads. We know the specific dangers of this corridor.',
         c1_title='Highway 31 Speeds Through Town', c1_text='Drivers maintain 55+ mph through Holly Pond\'s town limits despite homes, businesses, and pedestrians. The speed differential is deadly.',
         c2_title='School Zone Violations', c2_text='Holly Pond High School creates twice-daily surges in pedestrian traffic. Drivers who ignore reduced speed zones create serious danger for students.',
         c3_title='Pedestrians on Highway Shoulders', c3_text='Without sidewalks, residents walk on narrow highway shoulders inches from passing trucks and cars traveling at highway speed.',
         c4_title='Limited Crosswalks', c4_text='Holly Pond\'s town center along Highway 31 has few or no marked crosswalks. Residents cross without any designated safe crossing points.',
         c5_title='Poor Nighttime Lighting', c5_text='Sections of Highway 31 through Holly Pond lack adequate street lighting. After dark, pedestrians become nearly invisible.',
         c6_title='Intersection Dangers', c6_text='Where local streets meet Highway 31, turning vehicles focus on merging with traffic and fail to check for pedestrians crossing.',
         callout_bold='Speed kills pedestrians.', callout_text='A pedestrian struck at 55 mph has less than a 10% chance of survival. At 25 mph, survival rates exceed 90%. Ferguson &amp; Ferguson holds speeding drivers fully accountable.',
         step1='Call 911. Holly Pond Volunteer Fire and Cullman County EMS will respond. Alabama State Troopers or the Sheriff will document the scene.',
         step2='Go to Cullman Regional Medical Center immediately. Highway-speed pedestrian impacts cause life-threatening injuries requiring immediate evaluation.',
         step3='Photograph the scene, your injuries, the vehicle, highway conditions, and any lack of crosswalks or pedestrian signals. Get witness contact information.',
         why1_title='Highway 31 Corridor Expertise', why1_text='We understand the specific dangers of Highway 31 through Holly Pond and how speed, infrastructure, and driver behavior combine to injure pedestrians.'),

    dict(file='south-vinemont', city='South Vinemont', meta_desc='US-31 corridor pedestrian injuries and nighttime walking accidents.',
         image='https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=640&h=400&fit=crop',
         hero_lead='South Vinemont stretches along the US-31 corridor where limited lighting, no sidewalks, and high-speed traffic create some of Cullman County\'s most dangerous conditions for pedestrians &mdash; especially after dark.',
         intro_h2='The US-31 Corridor\'s Nighttime Pedestrian Danger Zone',
         intro_p1='South Vinemont is a community of about 700 people strung along US-31 in Cullman County. The highway is the lifeline of the community &mdash; but also its greatest danger. Residents live, shop, and visit neighbors along a corridor designed for through-traffic, not pedestrian activity.',
         intro_p2='What makes South Vinemont particularly dangerous is the lack of lighting. Long stretches of US-31 have no street lights whatsoever. After dark, pedestrians walking along shoulders or crossing the highway are virtually invisible. Nighttime pedestrian accidents here tend to be severe or fatal.',
         intro_p3='Ferguson &amp; Ferguson represents South Vinemont pedestrians injured along the US-31 corridor. We investigate lighting conditions, road design, and driver behavior to build cases that overcome Alabama\'s contributory negligence hurdle.',
         c1_title='Limited Highway Lighting', c1_text='Most of US-31 through South Vinemont has no street lights. Pedestrians after dark are nearly invisible, making nighttime walking extremely dangerous.',
         c2_title='High-Speed Through Traffic', c2_text='US-31 carries commuter and commercial traffic at 55+ mph. Drivers expect open highway, not pedestrians on shoulders or crossing the road.',
         c3_title='No Sidewalks or Shoulders', c3_text='South Vinemont\'s stretch of US-31 lacks adequate sidewalks and paved shoulders. Pedestrians walk on grass, gravel, or the road edge itself.',
         c4_title='Nighttime Visibility Failures', c4_text='No street lights, dark clothing, and high vehicle speed create conditions where drivers literally cannot see pedestrians until impact.',
         c5_title='Distracted Driving on Long Stretches', c5_text='US-31\'s long straight sections encourage phone use and inattention. Drivers on autopilot fail to scan for pedestrians in what they perceive as open road.',
         c6_title='Road Debris and Shoulder Hazards', c6_text='Gravel, broken pavement, and debris on road shoulders force pedestrians into the travel lane, directly into the path of high-speed traffic.',
         callout_bold='Darkness is not the pedestrian\'s fault.', callout_text='Insurance companies will blame you for walking at night or wearing dark clothing. Alabama law requires drivers to use headlights and exercise due care at all times. Ferguson &amp; Ferguson fights these victim-blaming tactics.',
         step1='Call 911. Cullman County EMS and the Sheriff will respond. If the accident happened at night, stress urgency &mdash; response times in dark rural areas can be longer.',
         step2='Get to Cullman Regional Medical Center immediately. Nighttime highway-speed impacts cause severe injuries requiring urgent evaluation.',
         step3='Photograph the scene including lighting conditions, road shoulders, your injuries, and the vehicle. Use your phone flash to document how little visibility exists.',
         why1_title='Nighttime Accident Expertise', why1_text='We know how to investigate nighttime pedestrian accidents &mdash; analyzing lighting conditions, headlight use, and visibility to prove driver negligence.'),

    dict(file='west-point', city='West Point', meta_desc='County road intersection pedestrian injuries and rural crossing accidents.',
         image='https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=640&h=400&fit=crop',
         hero_lead='West Point sits at the intersection of county roads where turning vehicles, poor sight lines, and no traffic signals create dangerous conditions for pedestrians at these uncontrolled crossroads.',
         intro_h2='Dangerous Crossroads in a Rural Community',
         intro_p1='West Point is a small Cullman County community of about 500 people situated where several county roads converge. These intersections &mdash; governed by stop signs rather than traffic signals &mdash; create particular hazards for pedestrians. Turning vehicles focus on merging with cross-traffic and frequently fail to check for people on foot.',
         intro_p2='Agricultural activity adds another dimension. Farm equipment approaching intersections blocks visibility for both pedestrians and drivers. Tractors making wide turns at crossroads can push pedestrians off the road or into the path of oncoming vehicles.',
         intro_p3='Ferguson &amp; Ferguson represents pedestrians injured at West Point\'s intersections and along its county roads. We understand how uncontrolled crossroads, agricultural traffic, and poor sight lines combine to create deadly conditions.',
         c1_title='Uncontrolled Intersection Dangers', c1_text='West Point\'s intersections rely on stop signs rather than traffic signals. Drivers rolling through stops strike pedestrians crossing at these intersections.',
         c2_title='Turning Vehicles Ignoring Pedestrians', c2_text='Drivers making turns at county road intersections focus on vehicle traffic and fail to scan for pedestrians in or near the crossroad.',
         c3_title='Poor Sight Lines at Crossroads', c3_text='Vegetation, terrain, and parked farm equipment block drivers\' views of approaching pedestrians until the last moment.',
         c4_title='Agricultural Vehicle Conflicts', c4_text='Tractors and farm equipment making wide turns at intersections force pedestrians off the road or into traffic lanes.',
         c5_title='Speeding Between Intersections', c5_text='Drivers accelerate aggressively between stop-sign intersections, reaching unsafe speeds on short stretches where pedestrians may be walking.',
         c6_title='No Pedestrian Crossings', c6_text='West Point has no marked crosswalks, pedestrian signals, or crossing infrastructure of any kind. Pedestrians cross entirely at their own judgment.',
         callout_bold='Stop signs protect vehicles, not pedestrians.', callout_text='Uncontrolled intersections give pedestrians zero protection. Drivers owe a duty of care to watch for people on foot at every intersection. Ferguson &amp; Ferguson holds them to that standard.',
         step1='Call 911. The Cullman County Sheriff will respond. Make sure a police report documents the intersection, traffic control, and conditions.',
         step2='Go to Cullman Regional Medical Center. Intersection impacts involve turning vehicles that can cause complex injuries.',
         step3='Photograph the intersection, sight lines, stop signs, vegetation blocking views, your injuries, and the vehicle. Document where you were when struck.',
         why1_title='Intersection Accident Expertise', why1_text='We understand how uncontrolled intersections, agricultural traffic, and poor sight lines contribute to West Point pedestrian accidents.'),
]

for c in cities:
    html = TEMPLATE.format(**c)
    path = os.path.join('pages', c['file'] + '.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Wrote {path}')

print('All pages generated.')
