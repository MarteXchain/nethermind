Passo 1
Rodar o node utilizando o arquivo mxt_rpc.cfg ( ./nethermind --config mxt_rpc.cfg )

Passo 2
Gerar a wallet com o comando:
curl -X POST   -H "Content-Type: application/json"   --data '{"jsonrpc":"2.0","method":"personal_newAccount","params":["tuasenhaaqui"],"id":1}'   http://localhost:8545

Passo 3
Anote o endereço gerado do comando anterior , coloque esse endereço no arquivo mxt_validator.cfg e crie o arquivo password.txt ( keystore/validator/password.txt ) com a senha que utilizou no comando anterior

Passo 4
Pare o node(mxt_rpc.cfg), e reinicie com o mxt_validator.cfg ( ./nethermind --config mxt_validator.cfg )

