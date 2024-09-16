# AISC0924-langgraph-demo-agent
LangGraph Demo Agent - AISC0924


### Setup Langgraph agent:

0) create the enviroment file 

```
cd langgraph-agent
cat > .env << EOF
TAVILY_API_KEY=<<>>
OPENAI_API_KEY=<<>>
EOF
```

1) Install dependencies:

```bash
pip install -r requirements.txt
```

2) Run in another terminal langgraph

```bash
langgraph test
```

after finish verify that there is one docker image running 

```
docker ps
```

3) Test with the script the agent

```
bash test.sh
```