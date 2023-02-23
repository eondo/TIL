- 프로젝트 목표 : 블록체인을 활용하여 탈중앙형 NFT 거래 플랫폼을 구축하는 것

# 기본 개념과 Ropsten 네트워크 실습

### Contents

1. 블록체인 분류
2. 이더리움 네트워크
3. Ropsten 실습 환경 준비
4. Ropsten 테스트넷 실습

## 블록체인의 분류

- 퍼블릭 : 대표적으로 Ethereum, 누구나 언제든 네트워크에 참여하고 탈퇴가 가능하다.
  - 관련 기술 : Bitcoin, Ethereum, Zcash, Litecoin, ...
- 프라이빗 : 하나의 조직 or 기관이 관장하는 네트워크로 승인된 주체만 자료를 읽고 지정 노드만 거래를 승인한다.
  - 관련 기술 : Quorum, MultiChain, Iroha, Monax, ...
- 컨소시엄 : 이해 관계자 간에 컨소시엄을 구성하여 네트워크를 구성, 네트워크 참여자에 의해 접근 허용한다.
  - 관련 기술 : Hyperledger Fabric, Tendermint, R3 Corda, Private Technologies, ...

## 이더리움 네트워크

### 퍼블릭 네트워크

- 메인넷, 테스트넷으로 구분
  - 메인넷 : 거래소에서 직접 사고 팔 수 있는 이더리움을 거래하고 그 위에서 스마트컨트랙트 등 다양한 Dapp을 개발할 수 있는 네트워크
  - 테스트넷 : 메인넷에 가기 전, 가볍게 시험해볼 수 있도록 이더리움 재단에서 제공하는 네트워크
  - 네트워크마다 네트워크 id가 있어서 id에 맞게 트랜잭션 보낼 수 있음
  - 이더리움넷에서 거래하는 코인과 다른 테스트넷인 곳에서 거래하는 코인은 가치가 매우 다름 -> 별개로 보기

### 프라이빗 네트워크

- 누구나 공개된 Client SW로 나만의 프라이빗 네트워크를 구축 가능
- besu는 엔터프라이즈 환경에 맞게 개량된 Hyperledger의 ethereum 프로젝트

## Ropsten 실습

1. MetaMask 설치
2. 계정 생성
3. 네트워크 연결
4. 테스트 이더 받기

### MetaMask

- 지갑 : 블록체인 네트워크를 사용할 수 있도록 블록체인의 데이터를 생성하거나 거래할 때 서명을 해야 하는데, 이러한 디지털 시그니처는 나의 pc에서만 접근할 수 있도록 계정의 개인키가 생성되어야 하고 이 개인키를 관리하는 프로그램이 '지갑'이다.
- 계정 생성 절차

1. 개인키 : 256bit의 무작위 숫자 -> 64자리의 Hex값으로 인코딩 == 매우 큰 숫자
2. 개인키로부터 공개키 생성
3. 공개키를 hash function 통해서 새로운 값으로 변환
4. 3 결과의 마지막 20바이트에 0x 붙이면 개인 이더리움 계정 주소

### MetaMask 지갑

#### 지갑 생성

#### 테스트 이더 받기

- 테스트 이더를 조금씩 제공하고 있으므로 faucet을 통해서 테스트넷 환경에서 사용할 수 있는 가치 없는 통화를 무료로 제공받을 수 있음 rETH, ROP

#### 테스트넷 실습

**🔷 MetaMask에서 트랜잭션 보내기**

- Account1 -> Test Wallet으로 0.01 eth 보내면 받은 내역에서 거래가 오고 감을 확인할 수 있다.
  **🔷 MetaMask Provider API 활용 실습**

#### Provider란?

클라이언트를 통해 이더리움 네트워크에 접근할 수 있도록 제공된 Javascript 객체

1. Ethereum Provider(인스턴스) 확인

- Ethereum Provider API의 페이지 방문 (https://docs.metamask.io/guide/ethereum-provider.html)
- 콘솔창에서 접속되어 있는 ethereum의 정보, 오브젝트를 확인할 수 있음

2. 연결 상태 확인
   `ethereum.isConnected()`
3. 이더리움 계정(지갑) 활성화 API
   `ethereum.enable()` : 사용할 지갑을 선택해서 계정에 연결하여 api가 지갑에 연결되어 있음을 설정할 수 있음
4. 활성화된 계정 확인
   `ethereum.selectedAddress` : 지갑 주소 변수 확인
5. Ethereum Provider로 RPC API 보내기 / 이더리움 네트워크에 직접 요청 보내기 -> 직접 RPC(Remote Procedure Call)를 콜
   `ethereum.request()`

- 지금 현재 네트워크에 block이 몇 개 쌓여있는지 물어보기

```js
ethereum
  .request({
    method: "eth_blockNumber",
    params: [],
  })
  .then((result) => console.log(result));
// 0x2cdd34
```

---

wei와 ether의 관계
RPC API를 사용한 소유 계정 잔액 확인

- RPC란?
  > 별도의 원격 제어를 위한 코딩 없이 다른 주소 공간에서 리모트의 함수나 프로시저를 실행 할 수 있게 해주는 프로세스간 통신
- 잔액 조회 관련 메서드
  https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getbalance

- 이더리움의 sign이란?
  이더리움에서의 트랜잭션의 종류
  - 암호화폐 송금
  - 컨트랙트 배포
  - 컨트랙트 호출

#### 이더리움 트랜잭션 담기는 정보 구조

| 항목               | 내용                                                       |
| ------------------ | ---------------------------------------------------------- |
| nonce              | 계정에서 발생시킨 트랜잭션의 누계                          |
| gasPrice, gasLimit | 트랜잭션을 실행할 때 지불해야 하는 가스 비용 정보          |
| to                 | 트랜잭션 수신 계정의 주소                                  |
| value              | 송금되는 ETH 금액(암호화폐를 송금할 때 사용)               |
| v, r, s            | 타원곡선암호(ECDSA)를 사용하는 송신 계정의 전자서명        |
| init               | 스마트 컨트랙트 코드(스마트 컨트랙트를 배포할 때 사용)     |
| data               | 스마트 컨트랙트 파라미터(스마트 컨트랙트를 실행할 때 사용) |

```js
function String2Hex(tmp) {
  var str = "hello ethereum";
  for (var i = 0; i < tmp.length; i++) {
    str += tmp[i].charCodeAt(0).toString(16);
  }
  return str;
}
```

- metamask에 request를 보내기 전 metamask 지갑을 연결하고 유저가 authorize하는 계좌를 가져와야 한다.

```js
const accounts = await ethereum.request({
  method: "eth_requestAccounts",
});
```

- transaction 보내기

```js
{
    "jsonrpc": "2.0",
    "method": "eth_sendTransaction",
    "params": [
        {
            "from": "0xf307806E792035604a67c772cCFdc1B5c78A1Cc7",
            "to": "0x23b502d73CEAFf78056f293531b0F884DA3f1dB7",
            "value": "0x9184e72a",
            "input": "^0x[68656c6c6f20657468657265756d]*$"
        }
    ],
    "id": 0
}
```

- RPC API를 사용하여 트랜잭션 보내기 결과 확인하기
  - `getTransactionByHash`
  - `getTransactionReceipt`
  - params : 트랜잭션의 hash값
- Transaction vs Transaction Receipt
  - `getTransactionByHash`의 결과
    ```js
    {
        "jsonrpc": "2.0",
        "result": {
            "accessList": [],
            "blockHash": "0x9b858dd31d3722791f935fb5fac71ce17a1cf7f8f70f8f0cbbbfe7500db21f43",
            "blockNumber": "0x2d07c4",
            "chainId": "0xaa36a7",
            "from": "0xf307806e792035604a67c772ccfdc1b5c78a1cc7",
            "gas": "0x7c5c",
            "gasPrice": "0x908a9047",
            "hash": "0x7ed79352e3d7670b83e56c6685639294c4540df2069a077712f559f4d0bd06fe",
            "input": "0x68656c6c6f20657468657265756d",
            "maxFeePerGas": "0x908a9048",
            "maxPriorityFeePerGas": "0x908a9040",
            "nonce": "0x2",
            "r": "0x4f37d6aa1d2152fbd9a2875dc068233cea326de546c8f397e588531ff942e673",
            "s": "0x4ca757b9dc6ea32f64cdba971b8bcdeeff2ee1535231ca3e213b5bddf001eca9",
            "to": "0x23b502d73ceaff78056f293531b0f884da3f1db7",
            "transactionIndex": "0x4",
            "type": "0x2",
            "v": "0x1",
            "value": "0x9184e72a"
        },
        "id": 0
    }
    ```
    - `getTransactionReceipt`의 결과
    ```js
      {
      "jsonrpc": "2.0",
      "result": {
          "blockHash": "0x9b858dd31d3722791f935fb5fac71ce17a1cf7f8f70f8f0cbbbfe7500db21f43",
          "blockNumber": "0x2d07c4",
          "contractAddress": null,
          "cumulativeGasUsed": "0x38976",
          "effectiveGasPrice": "0x908a9047",
          "from": "0xf307806e792035604a67c772ccfdc1b5c78a1cc7",
          "gasUsed": "0x52e8",
          "logs": [],
          "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "status": "0x1",
          "to": "0x23b502d73ceaff78056f293531b0f884da3f1db7",
          "transactionHash": "0x7ed79352e3d7670b83e56c6685639294c4540df2069a077712f559f4d0bd06fe",
          "transactionIndex": "0x4",
          "type": "0x2"
      },
      "id": 0
    }
    ```

#### getTransaction

- 토큰 생성 트랜잭션) to 필드가 비어있고, input 필드에 해당 컨트랙트 정보 존재
- 토큰 전송 트랜잭션) to 필드에 해당 컨트랙트 주소, input 필드에 호출된 컨트랙트 함수 정보 저장(function selector, parameters, ...)

#### getTransactionReceipt

- 트랜잭션이 블록체인 상에 deploy된 후에 생기는 것이 receipt 정보!
- 컨트랙트 생성 트랜잭션) contractAddress - 해당 주소, to필드는 비어있음
- 토큰 전송 트랜잭션) contractAddress는 보낼 토큰 주소 정보, to필드는 받는 주소 정보가 들어가있음
- pending 상태에서 receipt를 요청하면 Ethereum은 null을 반환한다. 즉, Ethereum에서 해당 Transaction이 commit된다면 receipt(거래 영수증)를 만들어낸다.

#### Transaction vs Transaction Receipt

- Transaction은 변경될 수 없는 데이터로 트랜잭션이 성공하거나 실패한 Transaction의 수행 결과가 Transaction Receipt으로 저장된다. 즉, 완결된 트랜잭션에 대해서만 Transaction Receipt이 생성된다.
