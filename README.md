# When Community Conversations Turn Into Work: A Taxonomy of Converted Discussions and Issues in GitHub
## Abstract
Popular and large contemporary open source projects now embrace a diverse set of documentation for communication channels. Examples include contribution guidelines (i.e, commit message guidelines, coding rules, submission guidelines), code of conduct (i.e., rules and behavior expectations), governance policies, and Q&A forum. In 2020, GitHub released Discussions to distinguish between communication and collaboration. However, it remains unclear how developers maintain these channels, how trivial, and the effort required to decide on the conversion. We conducted an empirical study on 259 NPM repositories, devising two taxonomies of reasons for converting discussions into issues and vice-versa. The most frequent conversion from discussion to issue is when developers request a contributor to clarify their idea into an issue (Clarification Request --35.1%), while agreeing that having non actionable topic  (QA, ideas, feature requests --55.0%) is the most frequent reason of converting an issue into discussion. Furthermore, we show that not all reasons for conversion are trivial (e.g., not a bug), and conversions potentially cost time (i.e., a median of 15.2 hours taken from issues to discussions). Our work contributes to how developers effectively utilize these different communication channels to maintain their collaboration. 

## Contents
* `RawData` - contains a list of NPM packages from the NPM registry (NPM.csv.zip) and all the discussion metadata from 259 repositories (All_discussion_data.zip).

* `Script` - contains the script to collect the GitHub discussion using GraphQL

## Authors
- [Dong Wang](https://dong-w.github.io/) - Kyushu University
- [Masanari Kondo](https://mkmknd.github.io/) - Kyushu University
- [Yasutaka Kamei](https://posl.ait.kyushu-u.ac.jp/~kamei/) - Kyushu University
- [Raula Gaikovina Kula](https://raux.github.io/) - Nara Institute of Science and Technology
- [Naoyasu Ubayashi](https://posl.ait.kyushu-u.ac.jp/~ubayashi/) - Kyushu University
