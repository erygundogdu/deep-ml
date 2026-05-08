import numpy as np

def train_sae(X, W_enc, W_dec, b_enc, lr: float, l1_coef: float, num_steps: int) -> float:
    """
    Train a ReLU sparse autoencoder with full-batch SGD and return the final loss.
    """
    # Your code here
    X = np.array(X)
    W_enc = np.array(W_enc)
    W_dec = np.array(W_dec)
    b_enc = np.array(b_enc)
    def ReLU(x): 
        return np.maximum(0,x)
    def loss(x_hat, z):
        rec = np.mean((x_hat - X) ** 2)
        sparse = l1_coef * np.sum(z, axis=1).mean()
        return rec + sparse
    for i in range(num_steps):
        scale = 2 / (X.shape[0] * X.shape[1])
        pre = X @ W_enc + b_enc
        z = ReLU(pre)
        x_hat = z @ W_dec
        dz = scale * (x_hat - X) @ W_dec.T + l1_coef / X.shape[0]
        
        W_enc_g = X.T @ (dz * (pre > 0))
        W_dec_g =   z.T @ (scale * (x_hat-X))
        b_enc_g = np.mean(dz * (pre>0)) * W_enc.shape[1]
        ###gradient update 
        W_enc = W_enc - lr * W_enc_g
        W_dec = W_dec - lr * W_dec_g
        b_enc = b_enc - lr * b_enc_g
    pre = X @ W_enc + b_enc
    z = ReLU(pre)
    x_hat = z @ W_dec
    loss_t = loss(x_hat,z)
    return float(loss_t)





    pass
