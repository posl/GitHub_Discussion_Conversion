# When Community Conversations Turn Into Work: A Taxonomy of Converted Discussions and Issues in GitHub
## Abstract
Popular and large contemporary open source projects now embrace a diverse set of documentation for communication channels. Examples include contribution guidelines (i.e, commit message guidelines, coding rules, submission guidelines), code of conduct (i.e., rules and behavior expectations), governance policies, and Q&A forum. In 2020, GitHub released Discussions to distinguish between communication and collaboration. However, it remains unclear how developers maintain these channels, how trivial, and the effort required to decide on the conversion. We conducted an empirical study on 259 NPM repositories, devising two taxonomies of reasons for converting discussions into issues and vice-versa. The most frequent conversion from discussion to issue is when developers request a contributor to clarify their idea into an issue (Clarification Request --35.1%), while agreeing that having non actionable topic  (QA, ideas, feature requests --55.0%) is the most frequent reason of converting an issue into discussion. Furthermore, we show that not all reasons for conversion are trivial (e.g., not a bug), and conversions potentially cost time (i.e., a median of 15.2 hours taken from issues to discussions). Our work contributes to how developers effectively utilize these different communication channels to maintain their collaboration. 

## Contents
* `RawData` - contains a list of NPM packages from the NPM registry (NPM.csv.zip) and all the discussion metadata from 259 repositories (All_discussion_data.zip).

* `Data Collector` - contains the py script to collect the GitHub discussions using GraphQL (Collector.py).

* `Label Data` - contains the manual label for those discussions that are suggested to be converted into issues (Discussion_to_Issue.csv) and those discussions that are converted from the existing issues (Issue_to_Discussion.csv). In addition, their related metadata are provided, including discussion comment, created time, comment time and so on. Note that `check_point' column refers to the manual mark whether this comment firstly raises the conversion intent or not.

* `github-retriever` - used to identify whether the exising issue is converted or not (https://github.com/sbaltes/github-retriever/).

## Appendix
Here, the rest of the three representative examples (issues that are converted into disucssions) would be shown:

<img width="487" alt="representtive_ex1" src="https://user-images.githubusercontent.com/28581719/184307135-226b6274-c355-4e53-9657-13ac8215a210.png">

* `(V) Already Fixed.` This category denotes the reason where the comment indicates that the issue has already been raised in either the issue lists or the discussion thread. As shown in the [Ex 6](https://github.com/gatsbyjs/gatsby/discussions/31283), the maintainer suggested that the pitfalls related to build has been addressed by adding a doc page and then converted the exising issue into a discussion thread.

<img width="487" alt="representtive_ex2" src="https://user-images.githubusercontent.com/28581719/184311254-289a11ee-02c0-4a88-b26f-2bcf7e709ff1.png">

* `(VI) Unrelated Repository.` This reason refers to the case where the comments indicate that the issue is not raised in the appropriate place. For instance, in the [Ex 7](https://github.com/facebook/create-react-app/discussions/11405), the author proposed an issue concerning task tracker app in the create-react-app repository. However, the collaborator considered that the issue was from CRA tool and furhter this issue was converted.

<img width="488" alt="representtive_ex3" src="https://user-images.githubusercontent.com/28581719/184312378-49c4d9d0-2ba3-451a-b19e-2477afb0d1ba.png">

* `(VII) Information Storage.` It means that the issue is converted since the comment indicates that the existing issue should be kept as a reference for the community. For example, in the [Ex 8](https://github.com/date-fns/date-fns/discussions/2841), the author raised a problem regarding react-native formatting and seeked for the solution. One collaborator provided a couple of solutions and later moved this issue into a discussion for other developers to find it easily.


## Authors
- [Dong Wang](https://dong-w.github.io/) - Kyushu University
- [Masanari Kondo](https://mkmknd.github.io/) - Kyushu University
- [Yasutaka Kamei](https://posl.ait.kyushu-u.ac.jp/~kamei/) - Kyushu University
- [Raula Gaikovina Kula](https://raux.github.io/) - Nara Institute of Science and Technology
- [Naoyasu Ubayashi](https://posl.ait.kyushu-u.ac.jp/~ubayashi/) - Kyushu University
