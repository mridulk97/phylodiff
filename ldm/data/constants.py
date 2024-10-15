DISENTANGLER_DECODER_OUTPUT = 'output'
DISENTANGLER_ENCODER_INPUT = 'in'
QUANTIZED_PHYLO_OUTPUT = 'zq_phylo'
DISENTANGLER_CLASS_OUTPUT = 'class'
QUANTIZED_PHYLO_NONATTRIBUTE_OUTPUT = 'zq_phylo_nonattribute'
DISENTANGLER_NON_ATTRIBUTE_TO_ATTRIBUTE_OUTPUT = 'nonattribate_to_attribute'
DISENTANGLER_NON_ATTRIBUTE_CLASS_OUTPUT = 'adversarial_classifier_output'
DISENTANGLER_ADV_MAPPING_OUTPUT = 'adversarial_mapping_output'
DISENTANGLER_ADV_LEARNING_OUTPUT = 'adversarial_learning_output'
NON_CLASS_TENSORS = [DISENTANGLER_ADV_LEARNING_OUTPUT, DISENTANGLER_ADV_MAPPING_OUTPUT, DISENTANGLER_ENCODER_INPUT, DISENTANGLER_DECODER_OUTPUT, QUANTIZED_PHYLO_OUTPUT, DISENTANGLER_NON_ATTRIBUTE_TO_ATTRIBUTE_OUTPUT, QUANTIZED_PHYLO_NONATTRIBUTE_OUTPUT, DISENTANGLER_NON_ATTRIBUTE_CLASS_OUTPUT]

CLASS_TENSORS = [DISENTANGLER_CLASS_OUTPUT]  

DATASET_CLASSNAME = 'class_name'

PHYLOCONFIG_KEY = "phylomodel_params"
LRFACTOR_KEY = "lr_factor"
LRCYCLE = "lr_cycle"
DISENTANGLERTYPE_KEY = 'disentangler_type'
COMPLETE_CKPT_KEY = "posttraining_ckpt"

HISTOGRAMS_FOLDER='code_histograms'
HISTOGRAMS_FILE="histograms.pkl"

DISENTANGLER_PHYLO_LOSS="/disentangler_phylo_loss"
TRANSFORMER_LOSS="/loss"
RECLOSS = "/rec_loss"
BASERECLOSS = "/base_true_rec_loss"

TEST_DIR="results_summary"

TSNE_FOLDER='tsne'