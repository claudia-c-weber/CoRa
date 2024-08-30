# CoRa - a parametric codon model for estimating conservative or radical amino acid substitutions

This repository contains notes on replicating results from Weber and Whelan, 2019 (https://doi.org/10.1093/molbev/msz003) using BppSuite (https://github.com/BioPP/bppsuite; Gu&#233;guen et al., 2013).

The folder ./scripts/run_models/ contains configuration information and scripts.

## Model basics

The CoRa model is specified by setting the `model` parameter to `CodonAAClustFreq(model=K80(),frequencies=F3X4)`. Other equilibrium frequency settings may also be used.

Custom amino acid partitions can also be specified. By default `partition=(1,2,3,3,3,2,2,1,2,4,4,2,4,4,1,3,3,2,2,1)`will be used. The order of the amino acids in the list is `ARNDCQEGHILKMFPSTWYV`, and the partitions indicate small non-polar, large polar, small polar, and large non-polar amino acids. 

## Prerequisites and configuration
The configuration files provided in this repository were tested with Bio++ v 2.4.0, and you will need to check out [this commit](https://github.com/BioPP/bpp-phyl/commit/64b6abc67d815ca062a90ed4390d457c83dc534b) of bpp-phyl in order to use the model. The structure of the configuration file has changed in more recent versions. See [here](https://github.com/BioPP/bppsuite/blob/master/Examples/MaximumLikelihood/Codons/M0/ML.bpp) for an example of how to set up M0 if you wish to use a newer version of Bio++. However, please be aware that I have not formally benchmarked this setup. 

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
