<html>
<h1>README</h1>
<p>This code implements constituency parse tree aggregation. </p>

<h2>Folder details</h2>

<ul>
<li><b>code:</b> This folder contains the code that implements constituency parse tree aggregation.</li>
<li><b>sample_dataset:</b> This folder contains 100 sentences from Penn Treebank dataset. This is the input for the method. Ground Truth is only used for evaluation purposes.</li>
</ul>

<h2>Code description</h2>

<ul>
<li><b>hanlp_resources.py:</b> The output of Hanlp parser follows a different format. This code is used to convert it into the format of other parsers. </li>
<li><b>resources.py:</b> This code does character indexing of the input, obtains cluster list and stores the formatted input into a dictionary.</li>
<li><b>compatibility.py:</b> This code contains implementation of maximum independent set.</li>
<li><b>medcpt.py:</b> This code does constituency parse tree aggregation.</li>
<li><b>evaluation.py:</b> This code does performance evaluation and stores the results as a dictionary file.</li>
<li><b>print_results.py:</b> This code prints evaluation results.</li>
</ul>

<h2>Input parsers</h2>

<ul>
<li><b>Berkeley:</b> The code to implement this parser can be found at https://pypi.org/project/benepar/ </li>
<li><b>CoreNLP:</b> The code to implement this parser can be found at https://stanfordnlp.github.io/CoreNLP/download.html </li>
<li><b>AllenNLP:</b> The code to implement this parser can be found at https://github.com/allenai/allennlp </li>
<li><b>Hanlp:</b> The code to implement this parser can be found at https://github.com/hankcs/HanLP/tree/master </li>
</ul>

<h2>Dataset details</h2>

<ul>
<li><b>Penn Treebank English:</b> The dataset can be found at https://catalog.ldc.upenn.edu/LDC99T42 </li>
<li><b>Ontonotes English:</b> The dataset can be found at https://catalog.ldc.upenn.edu/LDC2013T19 </li>
<li><b>Ontonotes Chinese:</b> The dataset can be found at https://catalog.ldc.upenn.edu/LDC2013T19 </li>
<li><b>Genia dataset:</b> The dataset can be found at https://github.com/allenai/genia-dependency-trees/tree/master/original_data </li>
<li><b>French Treebank:</b> The dataset can be found at http://ftb.llf-paris.fr/telecharger.php?langue=en </li>
<li><b>Tiger Corpus:</b> The dataset can be found at https://www.ims.uni-stuttgart.de/documents/ressourcen/korpora/tiger-corpus/download/start.html </li>
</ul>

<h2>Baseline Aggregation methods</h2>

<p>The implementation of baseline aggregation methods can be found at https://evolution.genetics.washington.edu/phylip/getme-new1.html</p>

<h2>Steps for code execution</h2>

<h3>Required packages</h3>

<ul>
<li>python 3</li>
<li>pickle</li>
<li>numpy</li>
</ul>

<h3>Execution flow</h3>

<ul>
<li>python resources.py</li>
<li>python medcpt.py</li>
<li>python evaluation.py</li>
<li>python print_results.py</li>
</ul>

  <h3> Citation </h3>
  <p>@misc{kulkarni2022cptam,
      title={CPTAM: Constituency Parse Tree Aggregation Method}, 
      author={Adithya Kulkarni and Nasim Sabetpour and Alexey Markin and Oliver Eulenstein and Qi Li},
      year={2022},
      eprint={2201.07905},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}</p>
  
</html>
