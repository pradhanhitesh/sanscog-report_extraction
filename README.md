# sanscog-report_extraction
 
<b>What is this study?</b>

CBR-SANSCOG study is a first-of-its-kind research project in India and one of the largest, longitudinal studies in the world conducted on the rural, aging population. This is a prospective, community-based, cohort study on healthy, aging individuals, 45 years and above (projected n = 10,000) hailing from the villages of Srinivaspura taluk (sub-district) located in Kolar district in the southern state of Karnataka, India. The study aims to identify risk and protective factors associated with cognitive changes due to normal ageing, dementia and other related disorders. This understanding will, in turn, help develop interventions to prevent or delay the onset of dementia, and therefore, improve quality of life of the elderly.

![alt text]([http://url/to/img.png](https://cbr.iisc.ac.in/wp-content/uploads/2021/05/sanscog-2.jpg))

I handle multimodal data such clinical, cognitive, blood biochemistry and especially, the multimodal neuroimaging data. However, handling neuroimaging data can be quite tricky and difficult, especially when the acquired neuroimaing modality has some discrepancies such as white matter hypointensities or lesion. In such scenario, it is important to remove those images from analysis. We rely on radiologists report to exclude subjects from analysis. However, going through more than 1000 radiologists report can be cumbersome and tiring. Hence, using Python, I automated the data-extraction process from PDF files, allowing me to review radiologists comment in a shorter amount of time and do the needful. 
