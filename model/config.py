from dataclasses import dataclass
@dataclass
class XENConfig:
    vocab_size:int=260
    max_seq_len:int=512
    d_model:int=384
    n_heads:int=6
    n_layers:int=8
    ffn_mult:float=2.6666666667
    dropout:float=0.0
    rope_theta:float=10000.0
    pad_token_id:int=0
    bos_token_id:int=1
    eos_token_id:int=2
    unk_token_id:int=3
    learning_rate:float=0.0003
    weight_decay:float=0.1
    max_grad_norm:float=1.0
