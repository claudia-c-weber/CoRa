# CoRa - a parametric codon model for estimating conservative or radical amino acid substitutions

Notes on replicating results from Weber and Whelan, 2019 (https://doi.org/10.1093/molbev/msz003) using BppSuite (https://github.com/BioPP/bppsuite; Gu&#233;guen et al., 2013).

The folder ./scripts/run_models/ contains configuration information and scripts.

## Comparison of results

Alignments from large-Ne taxa (blue) disfavour radical nonsynonymous substitutions, while small-Ne taxa (red) show a less pronounced pattern for both comparisons.

<img src="https://github.com/claudia-c-weber/CoRa/blob/master/Co_vs_Ra_bppml_mm.png" alt="" width=800>

Statistical support for CoRa over M0, as indicated by values falling above the vertical black line, is consistently stronger when Ne is large.

<img src="https://github.com/claudia-c-weber/CoRa/blob/master/LRTs.png" alt="" width=800>

Minor discrepancies in estimates may be driven by slight differences in optimisation, gap handling, lower bounds on parameter estimates and starting trees.

### If you would like to use the model, please cite:

Weber CC and Whelan S (2019) *Physicochemical Amino Acid Properties Better Describe Substitution Rates in Large Populations*. Molecular Biology and Evolution. 36 (4), pp. 679–690 https://doi.org/10.1093/molbev/msz003

Gu&#233;guen L. et al. (2013) *Bio++: Efficient Extensible Libraries and Tools for Computational Molecular Evolution*. Molecular Biology and Evolution. 30 (8), pp. 1745–1750 https://doi.org/10.1093/molbev/mst097

ModeloMatic's model selection function is now available in IQ-Tree: (http://www.iqtree.org/)
