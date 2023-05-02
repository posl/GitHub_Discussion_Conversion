# When Community Conversations Turn Into Work: A Taxonomy of Converted Discussions and Issues in GitHub
## Abstract
Popular and large contemporary open-source projects now embrace a diverse set of documentation for communication channels. Examples include contribution guidelines (i.e., commit message guidelines, coding rules, submission guidelines), code of conduct (i.e., rules and behavior expectations), governance policies, and Q&A forum. In 2020, GitHub released Discussion to distinguish between communication and collaboration. However, it remains unclear how developers maintain these channels, how trivial it is, and whether deciding on conversion takes time. We conducted an empirical study on 259 NPM and 148 PyPI repositories, devising two taxonomies of reasons for converting discussions into issues and vice-versa. The most frequent conversion from a discussion to an issue is when developers request a contributor to clarify their idea into an issue (Reporting a Clarification Request –35.1% and 34.7%, respectively), while agreeing that having non actionable topic (QA, ideas, feature requests –55.0% and 42.0%, respectively) is the most frequent reason of converting an issue into a discussion. Furthermore, we show that not all reasons for conversion are trivial (e.g., not a bug), and raising a conversion intent potentially takes time (i.e., a median of 15.2 and 35.1 hours, respectively, taken from issues to discussions). Our work contributes to complementing the GitHub guidelines and helping developers effectively utilize the

## Contents
* `RawData` - contains all the discussion metadata from 259 NPM repositories (All_discussion_data_NPM.zip) and 148 PyPI repositories (All_discussion_data_PyPI.zip).

* `Data Collector` - contains the py script to collect the GitHub discussions using GraphQL (Collector.py).

* `Label Data` - contains the manual label for those discussions that are suggested to be converted into issues (Discussion_to_Issue_NPM/PyPI.csv) and those discussions that are converted from the existing issues (Issue_to_Discussion_NPM/PyPI.csv). In addition, their related metadata are provided, including discussion comment, created time, comment time and so on. Note that `check_point' column refers to the manual mark whether this comment firstly raises the conversion intent or not.

* `github-retriever` - used to identify whether the exising issue is converted or not (https://github.com/sbaltes/github-retriever/).


## Authors
- [Dong Wang](https://dong-w.github.io/) - Kyushu University
- [Masanari Kondo](https://mkmknd.github.io/) - Kyushu University
- [Yasutaka Kamei](https://posl.ait.kyushu-u.ac.jp/~kamei/) - Kyushu University
- [Raula Gaikovina Kula](https://raux.github.io/) - Nara Institute of Science and Technology
- [Naoyasu Ubayashi](https://posl.ait.kyushu-u.ac.jp/~ubayashi/) - Kyushu University
